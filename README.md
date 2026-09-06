# Health Data Reporting Toolkit

A lightweight open-source toolkit for calculating, validating, and reporting common public-health indicators from simple CSV datasets.

## What it does

The toolkit currently supports:

- TB case detection rate
- Malaria incidence per 1,000 population
- HIV treatment coverage
- HIV incidence percentage
- Basic data-quality checks
- A simple summary report generated from CSV data

## Project structure

```text
health-data-reporting-toolkit/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── data/
│   └── sample_health_data.csv
├── docs/
│   └── indicators.md
├── excel/
│   └── health-data-reporting-toolkit.xlsx
├── src/
│   ├── __init__.py
│   ├── indicators.py
│   └── report.py
├── tests/
│   └── test_indicators.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt

## Quick start

1. Install Python 3.10 or later.
2. Download or clone this repository.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the sample report:

```bash
python src/report.py data/sample_health_data.csv
```

## Example indicators

### TB case detection rate

```text
notified TB cases / estimated incident TB cases × 100
```

### Malaria incidence per 1,000 population

```text
confirmed malaria cases / population × 1,000
```

### HIV treatment coverage

```text
people living with HIV on ART / estimated people living with HIV × 100
```

### HIV incidence percentage

```text
new HIV infections / population at risk × 100
```

## Data-quality checks

The reporting script flags:

- Missing values
- Negative values
- Zero or invalid denominators
- Percentages above 100% where applicable

## Important note

This toolkit is for analysis, learning, and routine reporting support. Indicator definitions can vary by national program, donor, reporting period, age group, or surveillance methodology. Always verify the official definition used by your Ministry of Health, WHO, UNAIDS, Global Fund, or other governing program before submitting official figures.

## Contributing

Contributions are welcome. Useful additions include:

- Maternal and child health indicators
- Vaccination coverage indicators
- Nutrition indicators
- Excel export
- Charts and dashboards
- DHIS2-compatible imports
- Country-specific indicator definitions

## License

MIT License. See `LICENSE`.
