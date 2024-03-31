
import math
import os
import random
import re
import sys


# Problem:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# eg. arr = [1,3,5,7,9]
# The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24. The function prints:
# 16 24



#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    output = []
    # start: 0 -> 1, 2, 3, 4
    # next: 1 -> 0, 2, 3, 5
    for i in range(5):
        total_sum = 0
        print(arr[:i], arr[i+1:])
        curr_array = arr[:i] + arr[i+1:]
        total_sum = sum(curr_array)
        # fill array first
        if i == 0:
            output.append(total_sum)
            output.append(total_sum)
        # get min
        if total_sum< output[0]:
            output[0] = total_sum
        # get max
        elif total_sum> output[1]:
            output[1] = total_sum
    print(f'{output[0]} {output[1]}')
    
if __name__ == '__main__':
    # arr = [1,2,3,4,5]
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)