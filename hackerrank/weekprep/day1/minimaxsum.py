""" 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers. 

Ex:
arr = [1,3,5,7,9]

Using 1+3+5+7 = 16, 3+5+7+9=24, we get:

16 24


combinations example:
[0, 1, 2, 3] -> [0, 2, 3, 4] -> [0, 1, 3, 4]
"""

import math

def miniMaxSum(arr):
    # Write your code here
    
    # if empty array, return 0s
    if len(arr) == 0:
        print(0, 0)
        return
    # else the minimum sum will bascially be all 4 elements summed minus the max, while the maximum will be all 4 elements summed minus the min.
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    print(min_sum, max_sum)




if __name__ == '__main__':
    arr = [1,3,5,7,9]
    miniMaxSum(arr)