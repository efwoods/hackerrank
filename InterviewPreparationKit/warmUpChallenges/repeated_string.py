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

    # Edge Case: substring does not contain 'a'
    substring_character_list = list(set(s))
    if substring_character_list.count('a') == 0:
        return 0
    
    # Edge Case: substring contains only a single 'a'.
    if len(s) == 1:
        return n

    if n < len(s):
        # Search the substring for the number of occurences of the character
        # 'a' up to length 'n'.
        sub_occurences = 0
        for stringIndex in range(0, n):
            if s[stringIndex] == 'a':
                sub_occurences += 1
        return sub_occurences
    else:
        # Search the substring for the number of occurences of the
        # character 'a'.
        sub_occurences = 0
        for stringIndex in range(0, len(s)):
            if s[stringIndex] == 'a':
                sub_occurences += 1

        factor_to_increase_s_by =  n // len(s)
        total_occurences = factor_to_increase_s_by * sub_occurences

        return total_occurences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
