import re
import unittest


def is_valid_email(email: str):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


class TestValidEmail(unittest.TestCase):
    # Test valid email: test@example.com

    def test_valid_email(self):
        # Test valid email: (missing '@'): testexample.com
        return self.assertTrue(is_valid_email('hristo@gmail.com'))

    def test_missing_domain(self):
        # Test valid email: (missing domain): test@.com
        return self.assertFalse(is_valid_email('test@.com'))

    def test_missing_userName(self):
        # Test valid email: (missing username): @example.com
        return self.assertFalse(is_valid_email('@example.com'))

    def test_empty_string(self):
        # Edge case: test empty string ''
        return self.assertFalse(is_valid_email(''))


if __name__ == '__main__':
    unittest.main()
