# Data source notes

The quantitative backtest uses small evaluation extracts derived from official or authoritative public data sources. These notes document the values used in the prompts and the held-out 2024 outcomes used for scoring.

## S&P 500

Source: Federal Reserve Bank of St. Louis FRED, series `SP500` (source series from S&P Dow Jones Indices LLC)

Official table:
https://fred.stlouisfed.org/data/SP500

Values used:
- 2019-12-31: 3230.78
- 2020-12-31: 3756.07
- 2021-12-31: 4766.18
- 2022-12-30: 3839.50
- 2023-12-29: 4769.83
- 2024-12-31 held-out actual: 5881.63

The 2024-12-31 value of 5881.63 is the final trading-day observation used as the held-out year-end actual.

## WTI crude oil

Source: Federal Reserve Bank of St. Louis FRED, monthly West Texas Intermediate (WTI) series `MCOILWTICO` (underlying source: U.S. Energy Information Administration)

Official table:
https://fred.stlouisfed.org/data/MCOILWTICO

December monthly-average values used:
- 2020-12: 47.02 USD/barrel
- 2021-12: 71.71 USD/barrel
- 2022-12: 76.44 USD/barrel
- 2023-12: 71.90 USD/barrel
- 2024-12 held-out actual: 70.12 USD/barrel

## U.S. CPI-U

Source: U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers (CPI-U)

December 2024 CPI news release:
https://www.bls.gov/news.release/archives/cpi_01152025.htm

December year-over-year rates used:
- 2020: 1.4%
- 2021: 7.0%
- 2022: 6.5%
- 2023: 3.4%
- 2024 held-out actual: 2.9%

The BLS December 2024 release reports that the all-items CPI-U increased 2.9% over the 12 months ending December 2024.

## Evaluation design

Historical values through 2023 were supplied directly to the models. The 2024 values above were withheld from the prompts and used only after the forecasts were recorded. The complete evaluation extracts are stored in `data/historical_inputs.csv` and `data/actual_results.csv`.
