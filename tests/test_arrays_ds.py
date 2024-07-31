"""Module to test reverseArray method from the arrays_ds module."""

import os
import sys
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, filename='test_arrays_ds_output.log')
sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from Prepare.Data_Structures.Arrays import arrays_ds

class TestArraysDS(unittest.TestCase):
    """This class contains tests that test the arrays_ds module.

    Args:
        unittest (module): This module enables testing within the class.
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_test_reverse_array(self):
        """This tests the reverseArrays method with a base case."""

        arr = [1, 2, 3, 4]
        result = arrays_ds.reverseArray(arr)
        self.assertEqual(result, [4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()

