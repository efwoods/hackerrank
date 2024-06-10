#!/bin/python3

import math
import os
import random
import re
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "../..")))
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    """
    This function returns the number of pairs of socks in a given pile.
    
    Args:
        n (int): The number of socks in the pile.
        ar (int array): The list of socks in the pile.
        
    Returns:
        pairs (int): The number of pairs of socks.
    """
    
    uniqueColorSet = set(ar)
    frequencyOfEachColorDict = {}
    pairs = 0
    
    for currentColor in uniqueColorSet:
        for pileIndex in range(0, n):
            if ar[pileIndex] == currentColor:
                try:
                    frequencyOfEachColorDict[currentColor] += 1
                except KeyError:
                    frequencyOfEachColorDict[currentColor] = 1

    for key, value in frequencyOfEachColorDict.items():
        pairs += value // 2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
