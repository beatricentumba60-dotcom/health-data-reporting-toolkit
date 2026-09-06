import unittest

from src.indicators import (
    hiv_incidence_percent,
    hiv_treatment_coverage,
    malaria_incidence_per_1000,
    tb_case_detection_rate,
)


class IndicatorTests(unittest.TestCase):
    def test_tb_case_detection_rate(self):
        self.assertAlmostEqual(tb_case_detection_rate(80, 100), 80.0)

    def test_malaria_incidence(self):
        self.assertAlmostEqual(malaria_incidence_per_1000(500, 10000), 50.0)

    def test_hiv_treatment_coverage(self):
        self.assertAlmostEqual(hiv_treatment_coverage(900, 1000), 90.0)

    def test_hiv_incidence(self):
        self.assertAlmostEqual(hiv_incidence_percent(10, 5000), 0.2)

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            malaria_incidence_per_1000(10, 0)


if __name__ == "__main__":
    unittest.main()
