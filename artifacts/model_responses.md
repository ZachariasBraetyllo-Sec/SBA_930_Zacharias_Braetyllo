# SBA 930 Model Responses

This artifact records the model outputs used in the quantitative forecasting evaluation.

Two prompt conditions were tested:

- **Baseline:** Simple forecasting instructions using historical values only.
- **Optimized:** Structured instructions requiring observations, assumptions, uncertainty, and a conservative point forecast.

The numeric forecasts extracted from these responses are stored in `data/model_forecasts.csv` and evaluated against held-out historical outcomes by `src/evaluate.py`.

---

# 1. ChatGPT Baseline Responses

## 1.1 S&P 500 Year-End Forecast

**Forecast: 5,250**

Using only the values provided, the series shows an overall upward trend despite one major decline in 2022. A conservative forecast based on the long-term growth pattern, rather than simply extending the strongest recent gain, would place the S&P 500 at approximately **5,250** for the final trading day of 2024.

**Extracted forecast:** 5250

---

## 1.2 WTI Crude Oil December Average Forecast

**Forecast: $72.50 per barrel**

Using only the values provided, WTI rose sharply from 2020 to 2022 and then declined modestly in 2023. Rather than extending either the earlier surge or the recent decline too aggressively, a conservative forecast would keep the December 2024 average near the recent range at approximately **$72.50 per barrel**.

**Extracted forecast:** 72.50

---

## 1.3 U.S. CPI December Year-over-Year Forecast

**Forecast: 2.5%**

Using only the values provided, inflation peaked in 2021–2022 and then declined sharply to 3.4% in 2023. A conservative forecast would continue that downward trend but assume the pace of decline slows rather than falls at the same rate, giving an estimate of approximately **2.5%** for December 2024.

**Extracted forecast:** 2.5

---

# 2. Claude Baseline Responses

## 2.1 S&P 500 Year-End Forecast

**Forecast: about 5,257**

I fitted a constant growth rate to the five year-end values. The average log growth from 2019 to 2023 is about 9.7% a year (about 10.2% in simple terms), since ln(4769.83 / 3230.78) divided by 4 is roughly 0.0973. Applying one more year of that growth to the 2023 value gives 4,769.83 × e^0.0973 ≈ 5,257.

This is a naive trend extrapolation, not a prediction. The yearly changes in your data swung widely, from about +26% to about −19%, with a standard deviation of roughly 21% in log terms. A one-standard-deviation range around the forecast is roughly 4,250 to 6,500, so the single number should not be treated as precise. Five data points can't capture what drives the index, such as earnings, interest rates, or shocks.

**Extracted forecast:** 5257

---

## 2.2 WTI Crude Oil December Average Forecast

**Forecast: about $73 per barrel**

The 2020 value of $47.02 looks like an outlier, a low base followed by a sharp rebound, so I didn't extrapolate that growth rate. Doing so would imply about $83, which seems too high given that prices flattened after 2021. Instead I took the average of the last three December values (71.71, 76.44, 71.90), which is about $73.35, and rounded to $73.

These three values stay within a narrow band (about $72-76), so a flat, mean-reverting forecast fits the more recent pattern better than a trend line.

The uncertainty is large. The last three values have a standard deviation of only about $2.70, but that is just three points, and the full four-year sample (including 2020) has a standard deviation near $14. A realistic range is roughly $60-$86, so the point estimate shouldn't be treated as precise. Oil prices respond to supply, demand, and geopolitical events that four data points cannot capture.

**Extracted forecast:** 73

---

## 2.3 U.S. CPI December Year-over-Year Forecast

**Forecast: about 2.4%**

Inflation peaked at 7.0% in December 2021 and has fallen since, with the latest drop (6.5% to 3.4%) much larger than the one before it. I modeled this as a continuing decline that slows down. The year-over-year ratios were about 0.93 (7.0 to 6.5) and 0.52 (6.5 to 3.4), which average about 0.72. Applying that to 3.4% gives roughly 2.4%.

Two simpler methods bracket this. A straight-line trend over the last three points implies about 1.6%, which would require the decline to continue at its recent pace. Holding at 3.4% assumes the fall stops entirely. I chose the decay estimate because the 2020 value of 1.4% suggests a plausible floor near pre-spike levels, so a continued steep drop seems less likely than a flattening.

The uncertainty is large. With only four points, and a sharp spike and reversal in the sample, a reasonable range is roughly 1.4% to 3.4%. These figures reflect a pattern in the numbers and cannot capture the underlying causes of inflation, so the forecast shouldn't be treated as precise.

**Extracted forecast:** 2.4

---

# 3. ChatGPT Optimized Responses

## 3.1 S&P 500 Year-End Forecast

**Observations:** The year-over-year changes were approximately **+16.3%, +26.9%, −19.4%, and +24.2%**. The overall direction is upward, but the series is volatile because one year contains a substantial decline.

**Assumption:** A conservative forecast should reflect the long-term upward tendency without simply repeating the strongest recent gain. Using a moderated growth rate of about **17%** from the 2023 level produces a forecast that stays within the historical growth pattern while accounting for volatility.

**Major uncertainty:** Five annual observations are too few to capture changes in earnings, interest rates, economic conditions, or unexpected market shocks.

**Final forecast: 5,581**

**Extracted forecast:** 5581

---

## 3.2 WTI Crude Oil December Average Forecast

**Observations:** The four December averages are 47.02, 71.71, 76.44, and 71.90. The full-series mean is about **66.77**, but the most recent three values cluster much more tightly around the low-to-mid 70s. The recent direction is slightly downward from the 2022 peak, while volatility across the full sample is elevated because 2020 is much lower than the later values.

**Assumption:** A conservative forecast should give more weight to the recent three-year range than to the unusually low 2020 value. Rather than extrapolating the latest decline, I would expect partial mean reversion around the recent cluster.

**Major uncertainty:** Oil prices can change sharply because of supply disruptions, geopolitical events, or demand shocks, none of which can be inferred from four annual observations.

**Final forecast: $72.00 per barrel**

**Extracted forecast:** 72

---

## 3.3 U.S. CPI December Year-over-Year Forecast

**Observations:** The series rose sharply from 1.4% in 2020 to 7.0% in 2021, remained elevated at 6.5% in 2022, then fell to 3.4% in 2023. The recent direction is clearly downward, but the earlier spike shows inflation can remain persistent after a large increase.

**Assumption:** A reasonable forecast should continue the disinflation trend while assuming the decline slows as inflation moves closer to lower historical levels. Rather than extending the 2022-to-2023 drop directly, I would expect a more moderate decline.

**Major uncertainty:** Inflation can change quickly because of energy prices, supply disruptions, monetary policy, or demand conditions, none of which are represented in these four observations.

**Final forecast: 2.8%**

**Extracted forecast:** 2.8

---

# 4. Claude Optimized Responses

## 4.1 S&P 500 Year-End Forecast

Observations (computed from the supplied values)

| Year | Level | YoY change |
| --- | ---: | ---: |
| 2020 | 3,756.07 | +16.3% |
| 2021 | 4,766.18 | +26.9% |
| 2022 | 3,839.50 | −19.4% |
| 2023 | 4,769.83 | +24.2% |

- **Direction:** up in 3 of 4 years, with a net gain of about 47.6% from 2019 to 2023. The average log growth is about 9.7% a year.
- **Volatility:** the yearly changes are large and uneven, ranging from −19.4% to +26.9%. The sample standard deviation of log changes is about 21%. The one down year (2022) erased about 19% of the prior year's level.

## Assumptions (not facts)

- Next year's change is a draw from a distribution similar to these four years.
- Four observations overstate the reliability of the 9.7% average, so I cut it roughly in half to about 4.9% for a conservative estimate. This is a judgment call, not a derived number.
- No trend or seasonality beyond the average yearly change.

## Major uncertainty

The main uncertainty is the high year-to-year volatility measured from only four data points. The average growth rate is estimated very imprecisely, and one bad year could flip the result. A one-standard-deviation range around the forecast is roughly 4,050 to 6,190, so the point estimate is not precise.

## Final forecast

**5,008**

(Calculated as 4,769.83 × e^0.0487 ≈ 5,008.)

**Extracted forecast:** 5008

---

## 4.2 WTI Crude Oil December Average Forecast

Observations (computed from the supplied values)

- **Year-over-year changes:** +52.5% (2021), +6.6% (2022), −5.9% (2023).
- **Direction:** a big rebound from 2020, then a flattening, with the latest move slightly down.
- **Mean:** $66.77 across all four years, or $73.35 across the last three.
- **Volatility:** the standard deviation is about $13.35 with 2020 included, but only about $2.68 for 2021-2023. The 2020 value of $47.02 is far below the rest and drives most of the spread.

## Assumptions (not facts)

- The 2020 value is an unusually low starting point, so its +52.5% rebound shouldn't be extrapolated.
- The 2021-2023 values describe a more relevant recent range, but with only three points I don't fully trust a low-volatility estimate, so I partly pull the forecast toward the four-year mean.
- No trend beyond the data. I average three reference points: the latest value ($71.90), the three-year mean ($73.35), and the four-year mean ($66.77). This weighting is a judgment call, not a derived rule.

## Major uncertainty

The volatility estimate depends heavily on whether 2020 is treated as an outlier or a normal part of the distribution: the standard deviation is about $2.68 without it and $13.35 with it. With four data points I can't tell which is the better guide to next year.

## Final forecast

**$71 per barrel**

(The average of 71.90, 73.35, and 66.77 is about $70.67.) A reasonable range is roughly $58 to $84, wide enough to reflect that uncertainty. The point estimate is a conservative central value, not a precise prediction.

**Extracted forecast:** 71

---

## 4.3 U.S. CPI December Year-over-Year Forecast

Observations (computed from the supplied values)

- **Year-over-year changes:** +5.6 percentage points (2021), −0.5 points (2022), −3.1 points (2023).
- **Direction:** inflation spiked to 7.0% in 2021 and has fallen for two straight years. The latest decline was the largest, and the 2023 level of 3.4% is still well above the 2020 level of 1.4%.
- **Decay ratios:** 6.5/7.0 ≈ 0.93 and 3.4/6.5 ≈ 0.52, averaging about 0.72.
- **Volatility:** the yearly changes are very uneven (a standard deviation of about 4.5 points), mostly because of the 2021 spike.

## Assumptions (not facts)

- The recent disinflation continues but slows, rather than repeating the 3.1-point drop, which would imply about 0.3%, below the 2020 level.
- I give 70% weight to a trend-decay estimate (3.4% × 0.72 ≈ 2.4%) and 30% to persistence, meaning inflation stays at 3.4%. Weighting the trend more reflects your instruction, but the exact weights are a judgment call, not a derived rule.
- The 1.4% value from 2020 acts as a loose floor, not a target.

## Major uncertainty

The main uncertainty is how persistent inflation turns out to be. The last three observations show the rate falling by very different amounts each year, so I can't tell whether the decline is steady, slowing, or about to stall. Four data points can't distinguish these.

## Final forecast

**2.7%**

(0.70 × 2.4% + 0.30 × 3.4% ≈ 2.7%.) A reasonable range is roughly 1.7% to 3.6%. This is a conservative central estimate, not a precise prediction.

**Extracted forecast:** 2.7

---

# Extracted Forecast Summary

| Model | Prompt Type | Metric | Forecast |
| --- | --- | --- | ---: |
| ChatGPT | Baseline | S&P 500 Year-End | 5250 |
| ChatGPT | Baseline | WTI December Average | 72.5 |
| ChatGPT | Baseline | CPI YoY December | 2.5 |
| Claude | Baseline | S&P 500 Year-End | 5257 |
| Claude | Baseline | WTI December Average | 73 |
| Claude | Baseline | CPI YoY December | 2.4 |
| ChatGPT | Optimized | S&P 500 Year-End | 5581 |
| ChatGPT | Optimized | WTI December Average | 72 |
| ChatGPT | Optimized | CPI YoY December | 2.8 |
| Claude | Optimized | S&P 500 Year-End | 5008 |
| Claude | Optimized | WTI December Average | 71 |
| Claude | Optimized | CPI YoY December | 2.7 |