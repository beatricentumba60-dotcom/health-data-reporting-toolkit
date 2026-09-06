"""Reusable public-health indicator calculations."""


def _validate_nonnegative(value: float, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} cannot be negative")


def _validate_denominator(value: float, name: str) -> None:
    _validate_nonnegative(value, name)
    if value == 0:
        raise ValueError(f"{name} cannot be zero")


def tb_case_detection_rate(notified_cases: float, estimated_incident_cases: float) -> float:
    """Return TB case detection rate as a percentage."""
    _validate_nonnegative(notified_cases, "notified_cases")
    _validate_denominator(estimated_incident_cases, "estimated_incident_cases")
    return notified_cases / estimated_incident_cases * 100


def malaria_incidence_per_1000(confirmed_cases: float, population: float) -> float:
    """Return malaria incidence per 1,000 population."""
    _validate_nonnegative(confirmed_cases, "confirmed_cases")
    _validate_denominator(population, "population")
    return confirmed_cases / population * 1000


def hiv_treatment_coverage(on_art: float, people_living_with_hiv: float) -> float:
    """Return HIV treatment coverage as a percentage."""
    _validate_nonnegative(on_art, "on_art")
    _validate_denominator(people_living_with_hiv, "people_living_with_hiv")
    return on_art / people_living_with_hiv * 100


def hiv_incidence_percent(new_infections: float, population_at_risk: float) -> float:
    """Return HIV incidence as a percentage of population at risk."""
    _validate_nonnegative(new_infections, "new_infections")
    _validate_denominator(population_at_risk, "population_at_risk")
    return new_infections / population_at_risk * 100
