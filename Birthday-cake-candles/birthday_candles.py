#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maximum = 0
    count = 1

    for i in range(len(ar)):
        
        if(maximum < ar[i]):
            maximum = ar[i]
            continue

        if (maximum == ar[i]):
            count += 1
        
    return count
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
