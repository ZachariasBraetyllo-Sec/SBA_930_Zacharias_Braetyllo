from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

def read_actuals():
    out = {}
    with open(DATA / "actual_results.csv", newline="") as f:
        for row in csv.DictReader(f):
            out[row["metric"]] = float(row["actual_value"])
    return out

def read_forecasts():
    rows = []
    with open(DATA / "model_forecasts.csv", newline="") as f:
        for row in csv.DictReader(f):
            raw = row["forecast_value"].strip()
            if not raw:
                continue
            row["forecast_value"] = float(raw)
            rows.append(row)
    return rows

def main():
    actuals = read_actuals()
    forecasts = read_forecasts()

    if not forecasts:
        raise SystemExit(
            "No forecasts entered. Fill forecast_value in data/model_forecasts.csv, then rerun."
        )

    detail = []
    grouped_abs_pct = defaultdict(list)

    for row in forecasts:
        metric = row["metric"]
        if metric not in actuals:
            continue
        forecast = row["forecast_value"]
        actual = actuals[metric]
        abs_error = abs(forecast - actual)
        ape = abs_error / abs(actual) * 100 if actual != 0 else float("nan")
        key = (row["model"], row["prompt_type"])
        grouped_abs_pct[key].append(ape)
        detail.append({
            "model": row["model"],
            "prompt_type": row["prompt_type"],
            "metric": metric,
            "forecast": round(forecast, 4),
            "actual": round(actual, 4),
            "absolute_error": round(abs_error, 4),
            "absolute_percentage_error": round(ape, 2),
        })

    with open(RESULTS / "forecast_evaluation.csv", "w", newline="") as f:
        fields = ["model","prompt_type","metric","forecast","actual","absolute_error","absolute_percentage_error"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(detail)

    summary = []
    for (model, prompt_type), errors in sorted(grouped_abs_pct.items()):
        mape = sum(errors) / len(errors)
        summary.append({
            "model": model,
            "prompt_type": prompt_type,
            "n_forecasts": len(errors),
            "mape_percent": round(mape, 2),
        })

    with open(RESULTS / "model_summary.csv", "w", newline="") as f:
        fields = ["model","prompt_type","n_forecasts","mape_percent"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(summary)

    # Before-vs-after optimization by model
    by_model = defaultdict(dict)
    for row in summary:
        by_model[row["model"]][row["prompt_type"]] = row["mape_percent"]

    optimization = []
    for model, vals in sorted(by_model.items()):
        if "baseline" in vals and "optimized" in vals:
            before = vals["baseline"]
            after = vals["optimized"]
            improvement = before - after
            pct_improvement = (improvement / before * 100) if before else 0.0
            optimization.append({
                "model": model,
                "baseline_mape_percent": before,
                "optimized_mape_percent": after,
                "mape_improvement_points": round(improvement, 2),
                "relative_improvement_percent": round(pct_improvement, 2),
            })

    with open(RESULTS / "optimization_comparison.csv", "w", newline="") as f:
        fields = [
            "model","baseline_mape_percent","optimized_mape_percent",
            "mape_improvement_points","relative_improvement_percent"
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(optimization)

    print(f"Wrote {RESULTS / 'forecast_evaluation.csv'}")
    print(f"Wrote {RESULTS / 'model_summary.csv'}")
    print(f"Wrote {RESULTS / 'optimization_comparison.csv'}")

if __name__ == "__main__":
    main()
