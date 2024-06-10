#!/bin/python3

"""This module contains a method that counts the number of valleys along
a path."""

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps: int, path: str) -> int:
    """A method that counts the number of valleys for a given path.

    Args:
        steps (int): The total number of steps in a path
        path (str): The string containing the path. U indicates an
                    upward step. D indicates a downward step.

    Returns:
        total_valleys (int): The number of valleys traversed.
    """
    
    # Map a D to -1 & U to +1
    # Keep a running sum and increment a valley variable each time the
    # sum is below zero.
    
    total_valleys = 0
    altitude = 0
    # for stepIndex in range(0, steps):
    #     if
    
    return total_valleys
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()