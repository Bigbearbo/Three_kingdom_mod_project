import unittest
from tools.preview_economy import estimate


class TestPreviewEconomy(unittest.TestCase):
    def test_full_strength_peacetime(self):
        self.assertEqual(estimate(120, 120, 0, 200, 600), {
            "maintenance": 100.0,
            "replenishment_fee": 0.0,
            "total": 100.0,
        })

    def test_replenishment_from_90_to_110(self):
        self.assertEqual(estimate(120, 90, 20, 200, 600), {
            "maintenance": 75.0,
            "replenishment_fee": 100.0,
            "total": 175.0,
        })

    def test_reject_invalid_replenishment(self):
        with self.assertRaises(ValueError):
            estimate(120, 90, 31, 200, 600)


if __name__ == "__main__":
    unittest.main()
