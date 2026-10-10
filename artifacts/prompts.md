# SBA 930 backtest prompts

Use the same prompts in ChatGPT and Claude. For each response, record only the single numeric forecast requested in `data/model_forecasts.csv`.

## Baseline prompts

### S&P 500
Using only the historical values below, forecast the S&P 500 closing level for the final trading day of 2024. Do not use or mention any information from 2024. Return one numeric forecast and a short explanation.

2019: 3230.78
2020: 3756.07
2021: 4766.18
2022: 3839.50
2023: 4769.83

### WTI crude oil
Using only the historical December monthly-average WTI crude oil prices below, forecast the December 2024 monthly average in dollars per barrel. Do not use or mention any information from 2024. Return one numeric forecast and a short explanation.

2020: 47.02
2021: 71.71
2022: 76.44
2023: 71.90

### U.S. CPI inflation
Using only the historical December year-over-year U.S. CPI inflation rates below, forecast the December 2024 year-over-year CPI inflation rate. Do not use or mention any information from 2024. Return one numeric forecast and a short explanation.

2020: 1.4%
2021: 7.0%
2022: 6.5%
2023: 3.4%

## Optimized prompts

Use these after the baseline prompts. These implement the optimization experiment.

### S&P 500 optimized
Act as a financial forecasting assistant. Use only the verified historical values supplied below and do not use any information from 2024. First identify the year-over-year direction and volatility in the series. Then produce a conservative point forecast for the final trading day of 2024. Separate observations from assumptions, state one major uncertainty, and return one final numeric forecast.

2019: 3230.78
2020: 3756.07
2021: 4766.18
2022: 3839.50
2023: 4769.83

### WTI crude oil optimized
Act as a financial forecasting assistant. Use only the verified historical December monthly-average WTI values below and do not use any information from 2024. Consider the mean, recent direction, and volatility rather than extrapolating one year mechanically. Separate observations from assumptions, state one major uncertainty, and return one final December 2024 monthly-average forecast in dollars per barrel.

2020: 47.02
2021: 71.71
2022: 76.44
2023: 71.90

### U.S. CPI inflation optimized
Act as an economic forecasting assistant. Use only the verified December year-over-year CPI values below and do not use any information from 2024. Give greater weight to the recent disinflation trend while acknowledging that inflation can be persistent. Separate observations from assumptions, state one major uncertainty, and return one final December 2024 year-over-year CPI forecast as a percentage.

2020: 1.4%
2021: 7.0%
2022: 6.5%
2023: 3.4%
