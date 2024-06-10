"""Module to tests the sales by match hackerrank interview question"""

# Imports
import unittest
import sys
import os
import logging

sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__)),".."))

# from tools.debug_decorator import debug
from InterviewPreparationKit.warmUpChallenges import sales_by_match

logging.basicConfig(level=logging.DEBUG)

class TestSalesByMatch(unittest.TestCase):
    """This class is used to hold the tests for the sales-by-match
    module.

    Args:
        unittest (module): This module is used to implement test cases.
    """

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test01_test_logging(self):
        logging.info("Logging is functional.")
        logging.info(sys.path)

    def test02_sales_by_match(self):
        result = sales_by_match.sockMerchant(5, [1,1,2,2,1])
        logging.info(f'pairs: {result}')

if __name__ == '__main__':
    unittest.main()
