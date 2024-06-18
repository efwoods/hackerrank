#!/bin/python3

"""This module contains the method miniMaxSum which, given five positive
integers, prints the minimum and maximum values of the sum of exactly
four of the five integers."""

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """Given an array of 5 positive integers, prints the minimum and
    maximum sums using four of the five integers.

    Args:
        arr (list int): This is a list of positive integers. The values
        of the integers are constrained between 1 and 1 billion
        inclusively on both extremes.

    Returns:
        This method has no return. The output is two space separated
        integers on a single line: the minimum and maximum sums using
        four of the five integers.
    """

    arr.sort()
    minimum_sum = sum(arr[:-1])
    maximum_sum = sum(arr[1:])
    print(f'{minimum_sum} {maximum_sum}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
