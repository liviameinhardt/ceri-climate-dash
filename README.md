# ISA Energia 26

Dashboard Streamlit para análise de risco de temperatura e vento em linhas de transmissão.

## Execução

Abra o painel de temperatura:

```bash
streamlit run Temperatura.py
```

O Streamlit vai detectar `pages/` automaticamente como página multipage.

## Dados esperados

O aplicativo lê os arquivos em `processed_data/`:

- `processed_data/temperature/risk_table_P90.csv`
- `processed_data/temperature/risk_table_P95.csv`
- `processed_data/temperature/risk_table_P99.csv`
- `processed_data/temperature/histograms.npz`
- `processed_data/wind/risk_table_P90.csv`
- `processed_data/wind/risk_table_P95.csv`
- `processed_data/wind/risk_table_P99.csv`
- `processed_data/wind/histograms.npz`
