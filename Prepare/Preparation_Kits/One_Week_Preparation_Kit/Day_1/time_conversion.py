#!/bin/python3

"""This module converts a string in 12 hour format to 24 hour format."""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """This method converts a string of time from 12 hour to 24 hour
    format.

    Args:
        s (str): This is a single string that represents time in 12 hour
        format: hh:mm:ssAM or hh:mm:ssPM.

    Returns:
        A single string that represents the input time converted to 24
        hour format.
    """

    time_code = s[-2:]
    hh_place = int(s[:2])
    s = s[:-2]

    if time_code == 'AM' and hh_place == 12:
        # 12:00:00AM -> 12:59:59AM replace s[:2] to '00' strip s[:-2]
        s = '00' + s[2:]
    elif time_code == 'PM' and hh_place < 12:
        # 01:00:00PM -> 11:59:59PM add 12 to s[:2] && strip s[:-2]
        s = str(hh_place + 12) + s[2:]

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
