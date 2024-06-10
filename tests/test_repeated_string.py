import unittest
import sys
import os

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from InterviewPreparationKit.warmUpChallenges import repeated_string

class TestRepeatedString(unittest.TestCase):
    """Class to test the module repeated_string

    Args:
        unittest (module): Module used to run test cases.
    """

    def setUp(self) -> None:
        """Method to set up variables before each test.
        """
        pass
    
    def tearDown(self) -> None:
        """Method to tear down variables after each test.
        """
        pass

    def test01_repeated_string(self):
        """Tests the default problem listed on HackerRank.
        """

        result = repeated_string.repeatedString(s ='abcac', n = 10)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()