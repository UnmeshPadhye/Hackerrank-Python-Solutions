#!/bin/python3

import os
import sys
import time
#
# Complete the timeConversion function below.
#
td = input()

pre_convert = time.strptime(td, '%I:%M:%S%p')
final_convert = time.strftime('%H:%M:%S', pre_convert)

print(final_convert)
