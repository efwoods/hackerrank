#!/bin/python3

"""This module contains a method that counts the number of valleys along
a path."""

import math
import os
import random
import re
import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename='counting_valleys_debug.log')

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def enter_valley(altitude: int, total_valleys: int):
    """Indicates when a valley is entered. Updates the altitude and the
    total number of valleys the user has encountered.

    Args:
        altitude (int): This is the current altitude.
        total_valleys (int): This is a total of the number of valleys
                             along a given path. 

    Returns:
        altitude (int): This is the current altitude.
        total_valleys (int): This is a total of the number of valleys
                             along a given path. 
    """

    altitude -= 1
    total_valleys += 1

    return altitude, total_valleys

def change_altitude(altitude: int, step: str) -> ValueError | int:
    """This method defines a change in the current altitude depending
    upon a step.

    Args:
        altitude (int): This is the current altitude above sea level.
        step (str): This is the current step to take. 'U' indicates an
                    increase in altitude. 'D' indicates a decrease in
                    altitude.
    Returns:
        altitude (int): This is the updated current altitude after
                        taking a step.
    """

    if step == 'U':
        altitude += 1
    elif step == 'D':
        altitude -= 1
    else:
        logging.error("step does not have a value of 'U' or 'D'")
        logging.info(f'step: {step}')
        return ValueError
    
    return altitude

def countingValleys(steps: int, path: str) -> int:
    """A method that counts the number of valleys for a given path.

    Args:
        steps (int): The total number of steps in a path
        path (str): The string containing the path. U indicates an
                    upward step. D indicates a downward step.

    Returns:
        total_valleys (int): The number of valleys traversed.
    """

    total_valleys = 0
    altitude = 0

    for stepIndex in range(0, steps):
        if altitude == 0 and path[stepIndex] == 'D':
            altitude, total_valleys = enter_valley(altitude, total_valleys)
        else:
            altitude = change_altitude(altitude=altitude, step=path[stepIndex])

    return total_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()