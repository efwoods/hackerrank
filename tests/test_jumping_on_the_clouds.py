"""Test module for jumping on the clouds module"""

import unittest
import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename='jumping_on_the_clouds_debug.log')

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from InterviewPreparationKit.warmUpChallenges import jumping_on_the_clouds

class TestJumpingOnTheClouds(unittest.TestCase):
    """Class to contain tests for the module jumping_on_the_clouds

    Args:
        unittest (module): Module used to run test cases for the class.
    """

    def setUp(self) -> None:
        """Performs set up operations before each test method.
        """
        pass

    def tearDown(self) -> None:
        """Performs tear down operations after each test method.
        """
        pass

    def test01_jumping_on_clouds_len_2(self):
        """Test of the base case where the array of c is [0, 0]
        """

        total_jumps = jumping_on_the_clouds.jumpingOnClouds([0,0])
        self.assertEqual(total_jumps, 1)

    def test02_jumping_on_clouds_len_3(self):
        """Test of the legal cases where the array of c is length 3.
        """

        total_jumps = jumping_on_the_clouds.jumpingOnClouds([0,0,0])
        self.assertEqual(total_jumps, 1)
        
        total_jumps = jumping_on_the_clouds.jumpingOnClouds([0,1,0])
        self.assertEqual(total_jumps, 1)

    def test03_jumping_on_clouds_len_greater_than_3(self):
        """Test of the legal cases where the length of the clouds > 3.
        """

        c = [0,0,0,0,0]
        total_jumps = jumping_on_the_clouds.jumpingOnClouds(c)
        self.assertEqual(total_jumps, 2)

        c = [0,0,1,0,0]
        total_jumps = jumping_on_the_clouds.jumpingOnClouds(c)
        self.assertEqual(total_jumps, 3)

        c = [0,0,0,1,0]
        total_jumps = jumping_on_the_clouds.jumpingOnClouds(c)
        self.assertEqual(total_jumps, 2)

if __name__ == '__main__':
    unittest.main()