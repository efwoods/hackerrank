#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    """Counts the number of occurences of the character 'a' in a string
    that is length n and built from units who are atomically the value
    of the string of 's'.

    Args:
        s (str): The substring to be elongated and searched for the
                 number of occurences of 'a'.
        n (int): The length to search.
    """

    # Increase the length of the substring to sufficiently meet the
    # length requirements of n.
    while len(s) < n:
        s += s
    
    # Search the string for the number of occurences of the character
    # 'a' up to the length of 'n'.
    total_occurences = 0
    for stringIndex in range(0, n):
        if s[stringIndex] == 'a':
            total_occurences += 1

    return total_occurences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
