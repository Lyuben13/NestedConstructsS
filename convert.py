import unittest


def convert_temperature(temp: float, scale: str):
    if scale == 'C':
        return temp * (9 / 5) + 32
    elif scale == 'F':
        return temp * (5 / 9) - 32
    else:
        raise ValueError('Unknown scale: use\'C\' or \'F\'')


# Unit Test
class TestConvertTempFunction(unittest.TestCase):
    #Convert F to C
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert_temperature(32, 'C'), 89.6)
        self.assertEqual(convert_temperature(212, 'C'), 413.6)

    #Convert C to F
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert_temperature(0, 'F'), -32.0)
        self.assertEqual(convert_temperature(100, 'F'), 23.555555555555557)

    #Test invalid scale
    def test_invalid_scale(self):
        with self.assertRaises(ValueError):
            convert_temperature(0, 'X')

    #Edge case: Test conveting -40%

