import unittest

from prime import is_prime

class Tests(unittest.TestCase):
    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))

    def test_3(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))

    def test_4(self):
        """Check that 55 is not prime."""
        self.assertFalse(is_prime(55))

    def test_5(self):
        """Check that 13 is prime."""
        self.assertTrue(is_prime(13))


if __name__ == '__main__':
    unittest.main()