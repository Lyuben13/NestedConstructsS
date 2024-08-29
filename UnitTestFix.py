import pytest
import unittest


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def reverse_string(s: str):
    return s[::-1]


def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Unit тестове
class TestPrimeFunction(unittest.TestCase):
    # Тест: 13 е просто число
    def test_prime_number(self):
        self.assertTrue(is_prime(13))

    # Тест: 4 не е просто число
    def test_non_prime_number(self):
        self.assertFalse(is_prime(4))

    # Тест: 1 не е просто число
    def test_one_is_not_prime(self):
        self.assertFalse(is_prime(1))

    # Тест: 2 е просто число
    def test_two_is_prime(self):
        self.assertTrue(is_prime(2))


class TestReverseFunction(unittest.TestCase):
    # Обратен ред на обикновена дума
    def test_reverse_simple_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    # Обратен ред на празен низ
    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(''), '')

    # Обратен ред на един символ
    def test_reverse_single_char(self):
        self.assertEqual(reverse_string('a'), 'a')


class TestFactorialFunction(unittest.TestCase):
    # Тест: Факториел от 5 е 120
    def test_factorial_of_five(self):
        self.assertEqual(factorial(5), 120)

    # Тест: Факториел на 0 е 1
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    # Тест: Факториел на отрицателно число хвърля ValueError
    def test_negative_factorial(self):
        with self.assertRaises(ValueError):
            factorial(-5)


# Стартиране на тестовете
if __name__ == '__main__':
    unittest.main()
