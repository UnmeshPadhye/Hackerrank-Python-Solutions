#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    dia1 = 0 #To store sum of diagonal 1
    dia2 = 0 #To store sum of diagnoal 2 
    length = len(arr) 

    for index in range(length):
        dia1 += arr[index][index]
        dia2 += arr[index][(length-index-1)]

    return abs(dia1 - dia2) #calculate and return absolute value of difference 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
