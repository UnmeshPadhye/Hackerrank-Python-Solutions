#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    d1 = 0 
    d2 = 0 
    d3 = 0

    for i in range(length):
        if(arr[i] != abs(arr[i])): #Negative counter
            d2 += 1
        elif(arr[i] == 0):  # o counter
            d3 += 1
        else:   #Positive Counter
            d1 += 1

    print (d1/length)
    print (d2/length)
    print (d3/length)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
