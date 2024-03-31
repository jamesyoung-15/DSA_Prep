#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    am_pm = s[len(s)-2:]
    time = s[:len(s)-2]
    hour = int(time[:2])
    # print(am_pm, time)
    
    if am_pm == "AM":
        if hour == 12:
            time = "00" + time[2:]
        return time
    else:
        if hour != 12:
            hour += 12
        time = str(hour) + time[2:]
        return time

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
    
    
    s = "03:01:00AM"
    result = timeConversion(s)
    print(result)
