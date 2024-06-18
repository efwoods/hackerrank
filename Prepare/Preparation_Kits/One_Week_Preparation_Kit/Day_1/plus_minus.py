#!/bin/python3

"""This module takes an array of integers, calculates the ratio of
positive, negative, and zero, and prints the result with up to six
significant figures."""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    """This method calculates the ratio of positive, negative, and zero
    values in a given array and prints the result with up to six
    significant figures.

    Args:
        arr (list int): This is an array of integers. The number of
        integers in the array are constrained between 1 and 100
        inclusive at both extremes. The values of the integers range
        from -100 to positive 100 inclusive at both extremes.

    Return:
        This method prints the ratios of positive, negative, and zero
        values within the array with precision up to six significant
        figures. Tolerance of four significant figures is acceptable.
    """

    positive_total = 0
    negative_total = 0
    zero_total = 0
    length_of_array = len(arr)

    for index in range(length_of_array):
        if arr[index] > 0:
            positive_total += 1
        elif arr[index] < 0:
            negative_total += 1
        else:
            zero_total += 1

    print('{:.6f}'.format(positive_total / length_of_array))
    print('{:.6f}'.format(negative_total / length_of_array))
    print('{:.6f}'.format(zero_total / length_of_array))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
