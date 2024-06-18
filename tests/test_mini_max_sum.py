"""This module is used to test the module mini_max_sum."""

import os
import sys
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, 
                    filename='test_mini_max_sum_output.log')

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from Prepare.Preparation_Kits.One_Week_Preparation_Kit.Day_1 import \
    mini_max_sum

class TestPlusMinus(unittest.TestCase):
    """This class is used to run unit tests.

    Args:
        unittest (module): This module is used to enable test cases.
    """

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test00_base_case(self):
        """This is a base case test of the miniMaxSum method."""
        arr = [1, 3, 5, 7, 9]
        mini_max_sum.miniMaxSum(arr)

if __name__ == '__main__':
    unittest.main()
