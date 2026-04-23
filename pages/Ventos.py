from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

RISK_DIR = Path("processed_data/wind")

RISK_FILES = {
    "local": {
        "P90": RISK_DIR / "risk_table_P90.csv",
        "P95": RISK_DIR / "risk_table_P95.csv",
        "P99": RISK_DIR / "risk_table_P99.csv",
    },
    "global": {
        "P90": RISK_DIR / "risk_table_P90_global.csv",
        "P95": RISK_DIR / "risk_table_P95_global.csv",
        "P99": RISK_DIR / "risk_table_P99_global.csv",
    },
}
HIST_FILE = RISK_DIR / "histograms.npz"

SCENARIOS = ["SSP1-2.6", "SSP2-4.5", "SSP3-7.0"]
DATE_RANGES = ["2021-2040", "2031-2050", "2041-2060"]

MODE_LABELS = {
    "local": "Local (percentil por linha)",
    "global": "Global (percentil único do Brasil)",
}


@st.cache_data(show_spinner=False)
def _load_risk_table_cached(path_str: str, mtime: float) -> pd.DataFrame:
    df = pd.read_csv(path_str)
    # The global tables were written with temperature-style column names.
    # Normalize to the wind schema expected by the rest of the page.
    if "limit_ms" not in df.columns and "limit_K" in df.columns:
        df = df.rename(columns={"limit_K": "limit_ms"}).drop(columns=["limit_C"], errors="ignore")
    return df


def load_risk_table(limit_name: str, mode: str = "local") -> pd.DataFrame:
    path = RISK_FILES[mode][limit_name]
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return _load_risk_table_cached(str(path), path.stat().st_mtime)


@st.cache_resource(show_spinner=False)
def load_histograms() -> dict:
    if not HIST_FILE.exists():
        return {}
    data = np.load(HIST_FILE, allow_pickle=True)
    lines = list(data["lines"])
    combos = list(data["combos"])
    counts = data["counts"]
    bin_edges = data["bin_edges"]
    total_samples = data["total_samples"]
    return {
        "lines": lines,
        "combos": combos,
        "line_to_idx": {name: i for i, name in enumerate(lines)},
        "combo_to_idx": {label: j for j, label in enumerate(combos)},
        "counts": counts,
        "bin_edges": bin_edges,
        "total_samples": total_samples,
    }


def build_first_section_table(
    df: pd.DataFrame, weights: dict[str, float], date_range: str
) -> pd.DataFrame:
    df_future = df[df["scenario"].isin(SCENARIOS)].copy()
    df_future = df_future[df_future["date_range"] == date_range].copy()

    grouped = (
        df_future.groupby(["linha", "scenario"], as_index=False)
        .agg(
            n_days_in_scenario=("days_exceeding", "sum"),
            limit_ms=("limit_ms", "first"),
        )
    )

    wide = (
        grouped.pivot(index="linha", columns="scenario", values="n_days_in_scenario")
        .reindex(columns=SCENARIOS)
        .fillna(0)
    )

    weighted_score = sum(wide[sc] * weights[sc] for sc in SCENARIOS)

    result = wide.reset_index().rename(
        columns={
            "linha": "line_name",
            "SSP1-2.6": "count_ssp1_2_6",
            "SSP2-4.5": "count_ssp2_4_5",
            "SSP3-7.0": "count_ssp3_7_0",
        }
    )

    limit_by_line = (
        df_future.groupby("linha", as_index=False)["limit_ms"]
        .first()
        .rename(columns={"linha": "line_name", "limit_ms": "wind_limit_ms"})
    )

    result = result.merge(limit_by_line, on="line_name", how="left")
    total_days = float(df_future["total_days"].dropna().iloc[0]) if not df_future.empty else np.nan
    result["pct_ssp1_2_6"] = (100 * result["count_ssp1_2_6"] / total_days).round(2)
    result["pct_ssp2_4_5"] = (100 * result["count_ssp2_4_5"] / total_days).round(2)
    result["pct_ssp3_7_0"] = (100 * result["count_ssp3_7_0"] / total_days).round(2)
    result["weighted_score"] = weighted_score.values
    result["rank"] = result["weighted_score"].rank(method="dense", ascending=False)

    result["wind_limit_ms"] = result["wind_limit_ms"].round(2)
    result["weighted_score"] = result["weighted_score"].round(2)
    result["rank"] = result["rank"].astype(int)

    return result.sort_values(["rank", "weighted_score"], ascending=[True, False]).reset_index(
        drop=True
    )


def build_tables_by_date_range(
    df: pd.DataFrame, weights: dict[str, float]
) -> dict[str, pd.DataFrame]:
    return {dr: build_first_section_table(df, weights, dr) for dr in DATE_RANGES}


def get_default_riskiest_line(tables: dict[str, pd.DataFrame]) -> str | None:
    all_scores = []
    for dr in DATE_RANGES:
        table = tables.get(dr)
        if table is None or table.empty:
            continue
        all_scores.append(table[["line_name", "weighted_score"]])
    if not all_scores:
        return None
    merged = pd.concat(all_scores, ignore_index=True)
    risk = merged.groupby("line_name", as_index=False)["weighted_score"].sum()
    risk = risk.sort_values("weighted_score", ascending=False)
    if risk.empty:
        return None
    return str(risk.iloc[0]["line_name"])


def get_line_percentile_limit_ms(df: pd.DataFrame, line_name: str) -> float | None:
    vals = df.loc[df["linha"] == line_name, "limit_ms"].dropna()
    if vals.empty:
        return None
    return float(vals.iloc[0])


def get_percentile_limits_ms_for_line(line_name: str, mode: str = "local") -> dict[str, float]:
    limits = {}
    for name in ["P90", "P95", "P99"]:
        df_lim = load_risk_table(name, mode=mode)
        v = get_line_percentile_limit_ms(df_lim, line_name)
        if v is not None:
            limits[name] = v
    return limits


def _get_hist_counts(
    hist: dict, line_name: str, scenario_label: str, date_range: str
):
    combo_key = f"{scenario_label}__{date_range}"
    i = hist["line_to_idx"].get(line_name)
    j = hist["combo_to_idx"].get(combo_key)
    if i is None or j is None:
        return None
    counts = hist["counts"][i, j, :]
    total = int(hist["total_samples"][i, j])
    if total == 0:
        return None
    return counts, total


def main() -> None:
    st.set_page_config(page_title="Painel de Risco de Ventos", layout="wide")
    st.title("Painel de Risco de Ventos")

    st.markdown(
        """
        Este painel permite comparar a exposição das linhas de transmissão a extremos de
        **vento máximo diário** sob diferentes cenários climáticos futuros. Use o
        seletor da barra lateral para alternar entre dois critérios de limiar:

        - **Local (percentil por linha):** cada linha usa como limiar o seu próprio
          percentil (P90/P95/P99) histórico (1995–2014). Responde à pergunta *"quantos
          dias no futuro a linha ultrapassa o que, para ela mesma, era um extremo?"*.
          Útil para avaliar **mudança local** em relação ao passado.
        - **Global (percentil único do Brasil):** o limiar P90/P95/P99 é calculado sobre
          a distribuição conjunta de todas as linhas no histórico, e o mesmo valor (em
          m/s) é aplicado a todas. Responde à pergunta *"quais linhas estão expostas aos
          ventos mais intensos em termos absolutos?"*. Útil para **ranquear linhas
          entre si** com um critério comum.
        """
    )

    st.sidebar.header("Filtros")
    mode = st.sidebar.radio(
        "Modo do limiar de percentil",
        options=["local", "global"],
        format_func=lambda m: MODE_LABELS[m],
        index=0,
        key="vento_mode",
        help=(
            "Local: o limiar P90/P95/P99 é calculado individualmente para cada linha "
            "a partir do seu próprio histórico — mede mudança em relação ao passado "
            "daquela linha. "
            "Global: o limiar é único para o Brasil (calculado sobre todas as linhas "
            "no histórico) — permite comparar linhas entre si em termos absolutos."
        ),
    )
    limit_name = st.sidebar.selectbox(
        "Percentil do limite de vento",
        options=["P90", "P95", "P99"],
        index=2,
    )

    st.sidebar.subheader("Pesos dos cenários")
    w1 = st.sidebar.number_input("Peso SSP1-2.6", min_value=0, value=1, step=1, key="vento_w1")
    w2 = st.sidebar.number_input("Peso SSP2-4.5", min_value=0, value=1, step=1, key="vento_w2")
    w3 = st.sidebar.number_input("Peso SSP3-7.0", min_value=0, value=1, step=1, key="vento_w3")

    weight_sum = w1 + w2 + w3
    if weight_sum <= 0:
        st.sidebar.error("At least one scenario weight must be greater than zero.")
        st.stop()

    weights = {
        "SSP1-2.6": w1 / weight_sum,
        "SSP2-4.5": w2 / weight_sum,
        "SSP3-7.0": w3 / weight_sum,
    }

    st.sidebar.caption(
        "Pesos brutos: "
        f"{int(w1)} {int(w2)} {int(w3)}  →  "
        "Pesos normalizados usados no rank: "
        f"SSP1-2.6={weights['SSP1-2.6']:.2f}, "
        f"SSP2-4.5={weights['SSP2-4.5']:.2f}, "
        f"SSP3-7.0={weights['SSP3-7.0']:.2f}"
    )

    df = load_risk_table(limit_name, mode=mode)
    tables_by_dr = build_tables_by_date_range(df, weights)

    st.header("Rank das linhas por excedência ponderada")
    st.write(
        "Cada aba mostra um horizonte temporal. O rank é calculado pela soma ponderada "
        "das contagens de cada cenário e depois rankeados em ordem decrescente."
    )


    with st.expander("Como o rank é calculado"):
        st.markdown(
            """
            Para cada linha de transmissão \(i\), calcula-se um **score agregado de risco climático** por meio da soma ponderada das contagens de dias acima do limiar em cada cenário:

            $$
            \t{score}_i =
            (n_{i,\mathrm{SSP1-2.6}} \cdot w_1) +
            (n_{i,\mathrm{SSP2-4.5}} \cdot w_2) +
            (n_{i,\mathrm{SSP3-7.0}} \cdot w_3)
            $$

            em que:

            - $n_{i,s}$ = número de dias em que os ventos máximos da linha \(i\) excedem o limiar no cenário \(s\);
            - $w_s$ = peso atribuído ao cenário \(s\), normalizado para que a soma dos pesos seja igual a 1.

            **Pesos adotados:**

            $$
            w_{\mathrm{SSP1-2.6}} = %.2f,\quad
            w_{\mathrm{SSP2-4.5}} = %.2f,\quad
            w_{\mathrm{SSP3-7.0}} = %.2f
            $$

            Em seguida, as linhas são ordenadas em função do escore calculado, em ordem decrescente:
            Assim, o **rank 1** corresponde à linha com maior exposição ponderada a excedências de vento no horizonte avaliado.
            """
            % (weights["SSP1-2.6"], weights["SSP2-4.5"], weights["SSP3-7.0"])
        )

    tabs = st.tabs(DATE_RANGES)
    for tab, dr in zip(tabs, DATE_RANGES):
        with tab:
            table = tables_by_dr[dr].copy()
            show_table = table.drop(
                columns=["weighted_score", "count_ssp1_2_6", "count_ssp2_4_5", "count_ssp3_7_0"],
                errors="ignore",
            )
            st.caption(
                "Cada linha representa uma transmissão. As colunas percentuais mostram "
                "a fração dos dias do intervalo em que a linha excedeu o limiar selecionado. "
                "O rank 1 indica maior risco ponderado nesta aba."
            )
            st.dataframe(
                show_table,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "line_name": st.column_config.TextColumn("Nome da linha"),
                    "wind_limit_ms": st.column_config.NumberColumn(
                        "Limite de vento (m/s)", format="%.2f"
                    ),
                    "pct_ssp1_2_6": st.column_config.NumberColumn("% dias SSP1-2.6", format="%.2f%%"),
                    "pct_ssp2_4_5": st.column_config.NumberColumn("% dias SSP2-4.5", format="%.2f%%"),
                    "pct_ssp3_7_0": st.column_config.NumberColumn("% dias SSP3-7.0", format="%.2f%%"),
                    "rank": st.column_config.NumberColumn("Rank", format="%d"),
                },
            )

    st.header("Distribuições da linha selecionada")

    hist = load_histograms()
    if not hist:
        st.warning(
            f"Arquivo de histogramas não encontrado em `{HIST_FILE.relative_to(ROOT)}`. "
            "Rode `python scripts/precompute_wind_histograms.py` para gerá-lo."
        )
        st.stop()

    default_key = f"vento_hist_default_line__{mode}"
    if default_key not in st.session_state:
        default_line = get_default_riskiest_line(tables_by_dr)
        st.session_state[default_key] = default_line
    else:
        default_line = st.session_state[default_key]

    if default_line is None:
        st.warning("Não há dados de linhas disponíveis para os filtros selecionados.")
        st.stop()

    line_options = sorted(df["linha"].dropna().astype(str).unique().tolist())
    default_index = line_options.index(default_line) if default_line in line_options else 0
    selected_line = st.selectbox(
        "Selecione a linha",
        options=line_options,
        index=default_index,
        key="vento_hist_selected_line",
    )

    percentile_limits = get_percentile_limits_ms_for_line(selected_line, mode=mode)
    if not percentile_limits:
        st.warning("Não foi possível determinar os limites percentuais (P90/P95/P99) para a linha selecionada.")
        st.stop()

    col1, col2, col3 = st.columns(3)
    col1.metric("Limite P90 (m/s)", f"{percentile_limits.get('P90', np.nan):.2f}")
    col2.metric("Limite P95 (m/s)", f"{percentile_limits.get('P95', np.nan):.2f}")
    col3.metric("Limite P99 (m/s)", f"{percentile_limits.get('P99', np.nan):.2f}")

    bin_edges = hist["bin_edges"]
    bin_widths = np.diff(bin_edges)

    fig, axes = plt.subplots(len(DATE_RANGES), 1, figsize=(11, 4 * len(DATE_RANGES)), sharex=True)
    if len(DATE_RANGES) == 1:
        axes = [axes]

    percentile_styles = {
        "P90": {"color": "black", "linestyle": "--"},
        "P95": {"color": "dimgray", "linestyle": "-."},
        "P99": {"color": "gray", "linestyle": ":"},
    }

    for ax, dr in zip(axes, DATE_RANGES):
        any_data = False
        for scenario in SCENARIOS:
            entry = _get_hist_counts(hist, selected_line, scenario, dr)
            if entry is None:
                continue
            counts, total = entry
            density = counts / (total * bin_widths)
            ax.step(bin_edges[:-1], density, where="post", linewidth=1.6, label=scenario)
            any_data = True

        for p_name, p_val in percentile_limits.items():
            style = percentile_styles.get(p_name, {"color": "black", "linestyle": "--"})
            ax.axvline(
                p_val,
                color=style["color"],
                linestyle=style["linestyle"],
                linewidth=1.5,
                label=f"{p_name} ({p_val:.2f} m/s)",
            )

        ax.set_title(f"{selected_line} | Distribuição do vento máximo diário ({dr})")
        ax.set_ylabel("Densidade")
        ax.grid(alpha=0.15)
        if any_data:
            ax.legend(loc="upper right", ncols=2, title="Cenários e limiares")
        else:
            ax.text(0.5, 0.5, "Sem dados disponíveis", ha="center", va="center", transform=ax.transAxes)

    fig.suptitle(
        f"Distribuições do vento máximo diário na linha {selected_line}",
        fontsize=14,
        y=1.02,
    )
    axes[-1].set_xlabel("Vento máximo diário (m/s)")
    for ax in axes:
        ax.set_xlim(0, float(bin_edges[-1]))

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


main()
