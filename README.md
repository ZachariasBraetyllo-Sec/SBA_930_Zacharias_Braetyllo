# SBA 930 - Evaluating LLMs for Financial Forecasting and Risk Analysis

This repository contains the reproducible technical artifacts requested for the SBA 930 resubmission.

## What is included

- verified historical inputs for the S&P 500, WTI crude oil, and U.S. CPI
- held-out 2024 actual outcomes
- identical baseline and optimized prompts for ChatGPT and Claude
- complete model responses and extracted numeric forecasts
- a quantitative evaluation script
- absolute error and absolute percentage error for each forecast
- model-level MAPE comparison
- before-versus-after optimization results
- the final revised report in `report/Zacharias_Braetyllo_SBA_930_REVISED.pdf`

## Method

The backtest uses historical values through the end of 2023 and treats 2024 as the held-out evaluation period.

Models were instructed to use only the supplied pre-2024 observations. Their complete responses are preserved in `artifacts/model_responses.md`, and the extracted numeric forecasts are stored in `data/model_forecasts.csv`.

The evaluation script compares each model forecast with the known 2024 actual value:

`forecast -> actual -> absolute error -> absolute percentage error`

The optimization experiment repeats the forecasts with a more structured prompt that adds verified-data constraints, explicit assumptions, uncertainty reporting, and task-specific analysis criteria. Baseline versus optimized MAPE is then compared.

## Data sources

- S&P 500: Federal Reserve Bank of St. Louis FRED, series `SP500` (source: S&P Dow Jones Indices LLC)
- WTI crude oil: FRED series `MCOILWTICO` / `WTISPLC` (source: U.S. Energy Information Administration / Federal Reserve Bank of St. Louis)
- CPI-U: U.S. Bureau of Labor Statistics

Detailed source references are documented in `artifacts/data_sources.md`.

The included CSV files are small evaluation extracts rather than full source datasets.

## Run

```bash
uv run python src/evaluate.py
```

The committed forecasts are already populated in:

```text
data/model_forecasts.csv
```

Generated files:

```text
results/forecast_evaluation.csv
results/model_summary.csv
results/optimization_comparison.csv
```

## Evaluation metric

Absolute Percentage Error (APE):

```text
|forecast - actual| / |actual| * 100
```

Mean Absolute Percentage Error (MAPE) is the mean APE across the evaluated indicators.

Lower error indicates a forecast closer to the held-out actual result.

## Limitation

Because modern LLMs may have been trained on or otherwise know historical 2024 outcomes, this is a classroom backtest rather than a fully leakage-proof forecasting benchmark. The prompts explicitly instruct both models to use only the supplied pre-2024 data.
