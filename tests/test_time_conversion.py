"""This module is used to test the module mini_max_sum."""

import os
import sys
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, 
                    filename='test_time_conversion_output.log')

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from Prepare.Preparation_Kits.One_Week_Preparation_Kit.Day_1 import \
    time_conversion

class TestPlusMinus(unittest.TestCase):
    """This class is used to run unit tests.

    Args:
        unittest (module): This module is used to enable test cases.
    """

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test00_midnight(self):
        """This is a test of conversion from 12 AM to 24-hour format."""
        s = "12:00:00AM"
        result = time_conversion.timeConversion(s)
        self.assertEqual(result, "00:00:00")

    def test01_one_afternoon(self):
        """This is a test of conversion of 1 PM to 24-hour format."""
        s = "01:00:00PM"
        result = time_conversion.timeConversion(s)
        self.assertEqual(result, "13:00:00")

    def test02_one_morning(self):
        """This is a test of conversion of 1 AM to 24-hour format."""
        s = "01:00:00AM"
        result = time_conversion.timeConversion(s)
        self.assertEqual(result, "01:00:00")

if __name__ == '__main__':
    unittest.main()
