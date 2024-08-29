import unittest


def calculate_total_price(prices: list[int], discount: int):
    if not 0 <= discount <= 100:
        raise ValueError('Discount must be between 0 and 100%')
    total = sum(prices)

    return total * (1 - discount / 100)


# Unit tests:
class TestTotalPriceFunction(unittest.TestCase):
    # Test no discount - 0% discount
    def test_no_discount(self):
        self.assertEqual(calculate_total_price([100, 200, 300], 0), 600)

    # Regular discount - 20% discount
    def test_full(self):
        self.assertEqual(calculate_total_price([10, 24, 30], 20), 51.2)

    # Empty cart - pass an empty list
    def test_empty_card(self):
        self.assertEqual(calculate_total_price([], 100), 0)

    # Invalid discount - 110% discount
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_total_price([100, 200], 110)

    # Full discount - 100%
    def test_full_discount(self):
        self.assertEqual(calculate_total_price([50, 50, 100], 100), 0)


if __name__ == '__main__':
    unittest.main()
