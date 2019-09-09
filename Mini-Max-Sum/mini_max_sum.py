#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    arr.sort()
    for i in range(len(arr)):
        sum += arr[i]
    
    print (sum - arr[4], sum - arr[0])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
