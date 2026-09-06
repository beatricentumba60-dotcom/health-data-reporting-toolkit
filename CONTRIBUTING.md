# Contributing to Health Data Reporting Toolkit

Thank you for your interest in contributing to the Health Data Reporting Toolkit.

This project aims to provide simple, transparent, and reusable tools for calculating, validating, and reporting common public-health indicators.

Contributions from developers, public-health professionals, data managers, researchers, students, and other interested contributors are welcome.

## Ways to Contribute

You can contribute by:

- Adding new public-health indicators
- Improving existing indicator calculations
- Adding or improving automated tests
- Improving the Excel toolkit
- Adding charts and dashboards
- Improving documentation
- Adding translations
- Improving data-quality checks
- Adding support for DHIS2-compatible data
- Reporting bugs
- Suggesting new features
- Improving country-specific documentation

## Reporting Bugs

If you find a problem:

1. Open the **Issues** section of this repository.
2. Create a new issue.
3. Describe the problem clearly.
4. Include the steps needed to reproduce it.
5. Include sample data when appropriate, but do not include confidential or personally identifiable health information.

## Suggesting a New Indicator

When proposing a new health indicator, please provide:

- Indicator name
- Numerator
- Denominator
- Calculation formula
- Unit of measurement
- Recommended interpretation
- Authoritative reference or source, when available

Indicator definitions may vary between countries and health programs, so references are particularly valuable.

## Contributing Code

1. Fork the repository.
2. Create a new branch for your change.
3. Make your changes.
4. Add or update tests when appropriate.
5. Run the tests locally.
6. Commit your changes with a clear message.
7. Push your branch to your fork.
8. Open a pull request.

## Running Tests

The project uses automated tests.

Run the test suite with:

    python -m unittest discover -s tests -p "test_*.py"

GitHub Actions also runs the tests automatically when changes are pushed or a pull request is opened.

## Excel Contributions

Changes to the Excel toolkit are also welcome.

Please describe:

- What was changed
- Which worksheet was affected
- Which formulas or indicators were modified
- How the change was tested

Avoid introducing macros unless there is a clear need and the security implications are documented.

## Data Privacy

Do not submit real patient-level data, personally identifiable information, confidential medical records, passwords, API keys, or other sensitive information to this repository.

Use synthetic or anonymized example datasets when demonstrating features.

## Documentation

Documentation improvements are welcome, particularly improvements that make the toolkit easier to use for health workers and data managers who may not have a programming background.

## Pull Requests

Keep pull requests focused on a specific improvement whenever possible.

Please explain:

- What the change does
- Why it is useful
- How it was tested
- Any limitations or assumptions

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License used by this repository.
