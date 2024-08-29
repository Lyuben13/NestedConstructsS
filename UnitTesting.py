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

    # # Unit test:
    # class TestPrimeFunction(unittest.TestCase):
    #     # Test that 13 is prime
    #     def test_prime_number(self):
    #         self.assertTrue(is_prime(13))
    #
    #     # Test that 4 is not prime
    #     def test_non_prime_number(self):
    #         self.assertFalse(is_prime(4))
    #
    #     # Test that 1 is not prime
    #     def test_one_is_note_prime(self):
    #         self.assertFalse(is_prime(1))
    #
    #     # Test that 2 is prime
    #     def test_two_is_prime(self):
    #         self.assertTrue(is_prime(2))

    # def test_prime_numbers():
    #     assert is_prime(13) == True
    #     assert is_prime(4) == False
    #     assert is_prime(1) == False
    #     assert is_prime(2) == True

    # def add_number(a: int, b: int):
    #     return a + b
    #
    #
    # # a = input("a = ")
    # # b = input("b = ")
    #
    # # number = add_number(int(a), int(b))
    # #
    # # print(number)
    #
    # # class TestAddFunction(unittest.TestCase):
    # #     def test_add_positive(self):
    # #         result = add_number(2, 3)
    # #         self.assertEqual(result, 5)
    # #
    # #     def test_add_negative_numbers(self):
    # #         result = add_number(-1, -1)
    # #         self.assertEqual(result, -2)
    # #
    # #     def test_add_zero(self):
    # #         result = add_number(0, 0)
    # #         self.assertEqual(result, 0)
    #
    #     #
    #     # class TestAddNumber(unittest.TestCase):
    #     #     def test_add(self):
    #     #         self.assertEqual(add_number(2, 3), 5)
    #     #         self.assertEqual(add_number(-1, 1), 0)
    #     #         self.assertEqual(add_number(0, 0), 0)
    #     #
    #     #
    #     # def test_add():
    #     #     assert add_number(2, 3) == 5
    #     #     assert add_number(-1, 1) == 0
    #     #     assert add_number(0, 0) == 0
    #
    #
    # def is_even(n):
    #     return n % 2 == 0
    #
    #
    # class TestEvenFunction(unittest.TestCase):
    #     def test_even_number(self):
    #         self.assertTrue(is_even(4))
    #
    #     def test_odd_number(self):
    #         self.assertFalse(is_even(3))

    #Unit test


#
# class TestReverseFunction(unittest.TestCase):
#     # Reverse a simple string 'hello'
#     def test_reverse_simple_string(self):
#         self.assertEqual(reverse_string('hello'), 'olleh')
#
#     # Reverse an empty string
#     def test_reverse_empty_string(self):
#         self.assertEqual(reverse_string(''), '')
#
#     # Reverse a single character string
#     def test_reverse_single_char(self):
#         self.assertEqual(reverse_string('a'), 'a')


class TestFactorialFunction(unittest.TestCase):
    # Test factorial of 5 is 120
    def test_factorial_of_five(self):
        self.assertEqual(factorial(5), 120)

    # Test the factorial of 0 is 1
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    # Test that the factorial of a negative number raises 'ValueError'
    def test_negative_factorial(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    if __name__ == '__main__':
        unittest.main()
