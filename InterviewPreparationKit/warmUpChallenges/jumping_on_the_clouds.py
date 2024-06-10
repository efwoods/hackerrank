#!/bin/python3

"""This module contains the solution to the 'Jumping on the Clouds' warm
up challenge on HackerRank."""

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def calculate_minimum_jumps(c: list[int], total_jumps: int = 0) -> int:
    """This method determines the minimum total number of jumps required
    in a given sequence "c". Values that are '0' are safe. Values that
    are '1' are unsafe and must be jumped over. The initial and final
    positions are always '0'. The goal is to count the number of jumps
    required to increase the index from array position zero to the
    length of the total array in the fewest number of jumps. Legal jump
    lengths are of one or two indices. 

    Args:
        c (list[int]): This is the list of integers. The first and last
                       integers are always '0'. 
        total_jumps (int): This is the total number of jumps taken. The 
                           value is initialized to zero whereas the
                           updated value is passed recursively through
                           the function.

    Returns:
        total_jumps (int): This is a global variable whose value indicates the
        minimum number of jumps required to reach the last index of the
        array of integers.
    """

    if len(c) == 1:
        return total_jumps
    elif len(c) == 2:
        total_jumps += 1
        return total_jumps
    else:
        if c[2] == 1:
            c = c[1:]
            total_jumps += 1
            return calculate_minimum_jumps(c, total_jumps)
        else:
            c = c[2:]
            total_jumps += 1
            return calculate_minimum_jumps(c, total_jumps)

def jumpingOnClouds(c) -> int:
    """This is the driver of the calculate_minimum_jumps method. It allows
    the total number of jumps to be initialized to zero and passed
    recursively calls of calculate_minimum_jumps.

    Args:
        c (list[int]): This list of integers represents the safety of
                       each landing spot of the jumper at each index. A
                       safe landing location is '0' whereas an unsafe
                       landing location is a '1'. The initial and final
                       indices in the array are always '0'. Legal jump 
                       lengths are of values of 1 or 2 indices.

    Returns:
        int: returns the total number of jumps taken to travers the
             array in the shortest number of possible jumps.
    """
    return calculate_minimum_jumps(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
