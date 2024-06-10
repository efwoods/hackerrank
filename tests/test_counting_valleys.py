"""Module used to test counting valleys module."""

# Imports
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                ".."))

from InterviewPreparationKit.warmUpChallenges import counting_valleys

class TestCountingValleys(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
