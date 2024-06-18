"""This module is used to test the module plus_minus."""

import os
import sys
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, filename='test_plus_minus_output.log')

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from Prepare.Preparation_Kits.One_Week_Preparation_Kit.Day_1 import plus_minus

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
        """This is a base case test of the plusMinus method."""

        arr = [-4, 3, -9, 0, 4, 1]
        plus_minus.plusMinus(arr)

if __name__ == '__main__':
    unittest.main()