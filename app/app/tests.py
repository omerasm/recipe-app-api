"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module."""
    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(6, 7)

        self.assertEqual(res, 13)

    def test_substract_numbers(self):
        """Test substracting numbers"""
        res = calc.substract(10, 3)

        self.assertEqual(res, 7)
