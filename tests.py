import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1,2), Fraction(1,4), Fraction(1,4)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_list_negative(self):
        data = [-1, -4, 6]
        result = sum(data)
        self.assertEqual(result, 1)