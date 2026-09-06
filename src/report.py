"""Generate a simple public-health indicator report from a CSV file."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from indicators import (
    hiv_incidence_percent,
    hiv_treatment_coverage,
    malaria_incidence_per_1000,
    tb_case_detection_rate,
)


def to_float(row: dict[str, str], key: str) -> float:
    value = row.get(key, "").strip()
    if value == "":
        raise ValueError(f"Missing value for {key}")
    return float(value)


def calculate_row(row: dict[str, str]) -> dict[str, float]:
    population = to_float(row, "population")
    return {
        "tb_case_detection_rate_pct": tb_case_detection_rate(
            to_float(row, "tb_notified_cases"),
            to_float(row, "tb_estimated_incident_cases"),
        ),
        "malaria_incidence_per_1000": malaria_incidence_per_1000(
            to_float(row, "malaria_confirmed_cases"), population
        ),
        "hiv_treatment_coverage_pct": hiv_treatment_coverage(
            to_float(row, "hiv_on_art"),
            to_float(row, "hiv_people_living_with_hiv"),
        ),
        "hiv_incidence_pct": hiv_incidence_percent(
            to_float(row, "hiv_new_infections"),
            to_float(row, "hiv_population_at_risk"),
        ),
    }


def main(csv_path: str) -> None:
    path = Path(csv_path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    if not rows:
        raise SystemExit("CSV contains no data rows")

    print("HEALTH DATA REPORT")
    print("=" * 70)

    for row in rows:
        area = row.get("area", "Unknown area")
        period = row.get("period", "Unknown period")
        print(f"\n{area} — {period}")
        try:
            indicators = calculate_row(row)
            print(f"TB case detection rate:     {indicators['tb_case_detection_rate_pct']:.2f}%")
            print(f"Malaria incidence:          {indicators['malaria_incidence_per_1000']:.2f} per 1,000")
            print(f"HIV treatment coverage:     {indicators['hiv_treatment_coverage_pct']:.2f}%")
            print(f"HIV incidence:              {indicators['hiv_incidence_pct']:.4f}%")

            warnings = []
            if indicators["tb_case_detection_rate_pct"] > 100:
                warnings.append("TB case detection rate exceeds 100%")
            if indicators["hiv_treatment_coverage_pct"] > 100:
                warnings.append("HIV treatment coverage exceeds 100%")
            if warnings:
                print("Warnings:")
                for warning in warnings:
                    print(f"  - {warning}")
        except (ValueError, TypeError) as exc:
            print(f"Data-quality error: {exc}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python src/report.py data/sample_health_data.csv")
    main(sys.argv[1])
