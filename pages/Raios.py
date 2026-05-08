from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent / "processed_data" / "raios"
PRED_FILE = ROOT / "all_lines_daily_cg_streamlit.parquet"

SCENARIO_MAP = {"ssp126": "SSP1-2.6", "ssp245": "SSP2-4.5", "ssp370": "SSP3-7.0"}
SCENARIOS = ["SSP1-2.6", "SSP2-4.5", "SSP3-7.0"]
DATE_RANGES = ["2021-2040", "2031-2050", "2041-2060"]

PROBA_THRESHOLDS = {
    "P50 (proba >= 0.50)": 0.50,
    "P70 (proba >= 0.70)": 0.70,
    "P90 (proba >= 0.90)": 0.90,
}

MODE_LABELS = {
    "fixed": "Probabilidade fixa (>= 0.5 / 0.7 / 0.9)",
    # "local": "Percentil local (por linha, sobre o proprio futuro)",
    # "global": "Percentil global (uma probabilidade unica para o Brasil)",
}


@st.cache_resource(show_spinner="Carregando previsoes diarias de raios...")
def load_predictions() -> pd.DataFrame:
    if not PRED_FILE.exists():
        st.error(f"Arquivo nao encontrado: {PRED_FILE}")
        return pd.DataFrame()
    df = pd.read_parquet(PRED_FILE)
    df["scenario"] = df["scenario"].map(SCENARIO_MAP).fillna(df["scenario"])
    df["date"] = pd.to_datetime(df["date"])
    return df


@st.cache_data(show_spinner=False)
def compute_threshold_value(
    mode: str, line: str | None, percentile: float, fixed_value: float
) -> dict[str, float]:
    """Devolve {linha: limiar de probabilidade}. Para modo fixo, mesmo valor para todas."""
    df = load_predictions()
    if df.empty:
        return {}
    if mode == "fixed":
        thr = float(fixed_value)
        return {ln: thr for ln in df["line"].unique()}
    if mode == "global":
        thr = float(np.quantile(df["proba"].to_numpy(), percentile))
        return {ln: thr for ln in df["line"].unique()}
    # local: por linha
    return df.groupby("line")["proba"].quantile(percentile).to_dict()


@st.cache_data(show_spinner="Calculando contagens por cenario e horizonte...")
def compute_exceedance_table(mode: str, percentile: float, fixed_value: float) -> pd.DataFrame:
    df = load_predictions()
    if df.empty:
        return df
    thr_by_line = compute_threshold_value(mode, None, percentile, fixed_value)
    thr_series = pd.Series(thr_by_line, name="thr")

    work = df.merge(thr_series.rename_axis("line").reset_index(), on="line", how="left")
    work["exceeds"] = (work["proba"] >= work["thr"]).astype(int)

    grouped = (
        work.groupby(["line", "scenario", "date_range"], as_index=False)
        .agg(days_exceeding=("exceeds", "sum"), total_days=("exceeds", "size"),
             thr=("thr", "first"))
    )
    return grouped


def build_first_section_table(
    grouped: pd.DataFrame, weights: dict[str, float], date_range: str
) -> pd.DataFrame:
    df_dr = grouped[grouped["date_range"] == date_range].copy()
    if df_dr.empty:
        return pd.DataFrame()

    wide = (
        df_dr.pivot_table(index="line", columns="scenario", values="days_exceeding", aggfunc="sum")
        .reindex(columns=SCENARIOS)
        .fillna(0)
    )
    weighted = sum(wide[s] * weights[s] for s in SCENARIOS)
    total_days = float(df_dr["total_days"].iloc[0]) if not df_dr.empty else np.nan
    thr_by_line = df_dr.groupby("line", as_index=False)["thr"].first()

    out = wide.reset_index().rename(
        columns={
            "line": "line_name",
            "SSP1-2.6": "count_ssp1_2_6",
            "SSP2-4.5": "count_ssp2_4_5",
            "SSP3-7.0": "count_ssp3_7_0",
        }
    )
    out = out.merge(thr_by_line.rename(columns={"line": "line_name", "thr": "proba_threshold"}),
                    on="line_name", how="left")
    out["pct_ssp1_2_6"] = (100 * out["count_ssp1_2_6"] / total_days).round(2)
    out["pct_ssp2_4_5"] = (100 * out["count_ssp2_4_5"] / total_days).round(2)
    out["pct_ssp3_7_0"] = (100 * out["count_ssp3_7_0"] / total_days).round(2)
    out["weighted_score"] = weighted.values
    out["rank"] = out["weighted_score"].rank(method="dense", ascending=False).astype(int)
    out["proba_threshold"] = out["proba_threshold"].round(3)
    out["weighted_score"] = out["weighted_score"].round(2)
    return out.sort_values(["rank", "weighted_score"], ascending=[True, False]).reset_index(drop=True)


def get_default_riskiest_line(tables: dict[str, pd.DataFrame]) -> str | None:
    parts = [t[["line_name", "weighted_score"]] for t in tables.values() if not t.empty]
    if not parts:
        return None
    s = pd.concat(parts).groupby("line_name")["weighted_score"].sum().sort_values(ascending=False)
    return None if s.empty else str(s.index[0])


def main() -> None:
    st.set_page_config(page_title="Painel de Risco de Raios", layout="wide")
    st.title("Painel de Risco de Raios")

    df = load_predictions()
    if df.empty:
        st.error(
            f"Arquivo de previsoes nao encontrado em `{PRED_FILE.relative_to(ROOT)}`. "
            "Rode o pipeline de previsao de raios para gera-lo."
        )
        st.stop()

    st.markdown(
        """
        Este painel mostra a exposicao das linhas de transmissao a **dias com alta
        probabilidade prevista de raios CG** (cloud-to-ground) em diferentes cenarios e
        horizontes climaticos. Os valores sao saidas de um classificador diario por linha
        — `proba` em [0, 1] e a probabilidade de ocorrencia de raio CG no buffer da LT
        naquele dia.

        Como o modelo so foi rodado nos cenarios futuros, o limiar para "dia de risco" e
        definido aqui de tres formas:

        - **Probabilidade fixa** (>= 0.50 / 0.70 / 0.90): interpretavel diretamente.
        - **Percentil local**: cada linha usa o seu proprio percentil sobre os 40 anos
          futuros (mede mudanca relativa ao seu padrao).
        - **Percentil global**: percentil unico calculado sobre todas as linhas
          (compara linhas entre si em termos absolutos).
        """
    )

    st.sidebar.header("Filtros")
    mode = st.sidebar.radio(
        "Definicao do limiar",
        options=list(MODE_LABELS.keys()),
        format_func=lambda m: MODE_LABELS[m],
        index=0,
        key="raios_mode",
    )

    if mode == "fixed":
        thr_label = st.sidebar.selectbox(
            "Limiar de probabilidade", list(PROBA_THRESHOLDS.keys()), index=1,
        )
        fixed_value = PROBA_THRESHOLDS[thr_label]
        percentile = 0.0
    else:
        pct_label = st.sidebar.selectbox(
            "Percentil", ["P90", "P95", "P99"], index=2,
        )
        percentile = {"P90": 0.90, "P95": 0.95, "P99": 0.99}[pct_label]
        fixed_value = 0.0
        thr_label = pct_label

    st.sidebar.subheader("Pesos dos cenarios")
    w1 = st.sidebar.number_input("Peso SSP1-2.6", min_value=0, value=1, step=1, key="raios_w1")
    w2 = st.sidebar.number_input("Peso SSP2-4.5", min_value=0, value=1, step=1, key="raios_w2")
    w3 = st.sidebar.number_input("Peso SSP3-7.0", min_value=0, value=1, step=1, key="raios_w3")
    weight_sum = w1 + w2 + w3
    if weight_sum <= 0:
        st.sidebar.error("Pelo menos um peso deve ser maior que zero.")
        st.stop()
    weights = {
        "SSP1-2.6": w1 / weight_sum,
        "SSP2-4.5": w2 / weight_sum,
        "SSP3-7.0": w3 / weight_sum,
    }
    st.sidebar.caption(
        f"Pesos brutos: {int(w1)} {int(w2)} {int(w3)}  ->  "
        f"Pesos normalizados: SSP1-2.6={weights['SSP1-2.6']:.2f}, "
        f"SSP2-4.5={weights['SSP2-4.5']:.2f}, SSP3-7.0={weights['SSP3-7.0']:.2f}"
    )

    grouped = compute_exceedance_table(mode, percentile, fixed_value)
    tables_by_dr = {dr: build_first_section_table(grouped, weights, dr) for dr in DATE_RANGES}

    st.header("Rank das linhas por excedencia ponderada")
    st.write(
        "Cada aba mostra um horizonte temporal. O rank e calculado pela soma ponderada "
        "dos dias com probabilidade prevista acima do limiar selecionado."
    )

    with st.expander("Como o rank e calculado"):
        st.markdown(
            f"""
            Para cada linha \\(i\\):
            $$
            \\text{{score}}_i =
            n_{{i,\\mathrm{{SSP1\\text{{-}}2.6}}}} w_1 +
            n_{{i,\\mathrm{{SSP2\\text{{-}}4.5}}}} w_2 +
            n_{{i,\\mathrm{{SSP3\\text{{-}}7.0}}}} w_3
            $$

            em que $n_{{i,s}}$ e o numero de dias do horizonte em que a probabilidade
            prevista de raio CG na linha excede o limiar selecionado, e $w_s$ os pesos
            normalizados.

            **Limiar:** {thr_label}

            **Pesos adotados:**
            $$
            w_{{\\mathrm{{SSP1\\text{{-}}2.6}}}} = {weights['SSP1-2.6']:.2f},\\quad
            w_{{\\mathrm{{SSP2\\text{{-}}4.5}}}} = {weights['SSP2-4.5']:.2f},\\quad
            w_{{\\mathrm{{SSP3\\text{{-}}7.0}}}} = {weights['SSP3-7.0']:.2f}
            $$
            """
        )

    tabs = st.tabs(DATE_RANGES)
    for tab, dr in zip(tabs, DATE_RANGES):
        with tab:
            table = tables_by_dr[dr]
            if table.empty:
                st.info("Sem dados para este horizonte."); continue
            show = table.drop(
                columns=["weighted_score", "count_ssp1_2_6", "count_ssp2_4_5", "count_ssp3_7_0"],
                errors="ignore",
            )
            st.caption(
                "As colunas percentuais mostram a fracao dos dias do intervalo em que "
                "a linha excedeu o limiar. Rank 1 = maior risco ponderado."
            )
            st.dataframe(
                show,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "line_name": st.column_config.TextColumn("Nome da linha"),
                    "proba_threshold": st.column_config.NumberColumn(
                        "Limiar de probabilidade", format="%.3f"),
                    "pct_ssp1_2_6": st.column_config.NumberColumn("% dias SSP1-2.6", format="%.2f%%"),
                    "pct_ssp2_4_5": st.column_config.NumberColumn("% dias SSP2-4.5", format="%.2f%%"),
                    "pct_ssp3_7_0": st.column_config.NumberColumn("% dias SSP3-7.0", format="%.2f%%"),
                    "rank": st.column_config.NumberColumn("Rank", format="%d"),
                },
            )

    st.header("Distribuicao da probabilidade prevista por linha")

    default_key = f"raios_default_line__{mode}__{thr_label}"
    if default_key not in st.session_state:
        st.session_state[default_key] = get_default_riskiest_line(tables_by_dr)
    default_line = st.session_state[default_key]

    line_options = sorted(df["line"].dropna().astype(str).unique().tolist())
    if default_line is None:
        default_line = line_options[0]
    default_index = line_options.index(default_line) if default_line in line_options else 0
    selected_line = st.selectbox(
        "Selecione a linha", options=line_options, index=default_index,
        key="raios_selected_line",
    )

    df_line = df[df["line"] == selected_line]
    thr_by_line = compute_threshold_value(mode, selected_line, percentile, fixed_value)
    line_thr = float(thr_by_line.get(selected_line, fixed_value))

    col1, col2, col3 = st.columns(3)
    col1.metric("Limiar usado", f"{line_thr:.3f}")
    col2.metric("Dias totais (linha, todos cenarios/horizontes)", f"{len(df_line):,}")
    col3.metric("% dias acima do limiar",
                f"{100 * (df_line['proba'] >= line_thr).mean():.2f}%")

    bin_edges = np.linspace(0.0, 1.0, 41)
    fig, axes = plt.subplots(len(DATE_RANGES), 1, figsize=(11, 4 * len(DATE_RANGES)),
                             sharex=True)
    if len(DATE_RANGES) == 1:
        axes = [axes]

    for ax, dr in zip(axes, DATE_RANGES):
        any_data = False
        for scenario in SCENARIOS:
            mask = (df_line["scenario"] == scenario) & (df_line["date_range"] == dr)
            vals = df_line.loc[mask, "proba"].to_numpy()
            if vals.size == 0:
                continue
            counts, _ = np.histogram(vals, bins=bin_edges, density=True)
            ax.step(bin_edges[:-1], counts, where="post", linewidth=1.6, label=scenario)
            any_data = True

        ax.axvline(line_thr, color="black", linestyle="--", linewidth=1.5,
                   label=f"limiar ({line_thr:.3f})")
        ax.set_title(f"{selected_line} | Probabilidade diaria de raio CG ({dr})")
        ax.set_ylabel("Densidade")
        ax.grid(alpha=0.15)
        if any_data:
            ax.legend(loc="upper right", title="Cenarios e limiar")
        else:
            ax.text(0.5, 0.5, "Sem dados disponiveis", ha="center", va="center",
                    transform=ax.transAxes)

    fig.suptitle(f"Distribuicoes da probabilidade diaria de raios — {selected_line}",
                 fontsize=14, y=1.02)
    axes[-1].set_xlabel("Probabilidade prevista (modelo)")
    for ax in axes:
        ax.set_xlim(0.0, 1.0)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


main()
