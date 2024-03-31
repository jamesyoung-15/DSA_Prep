import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    hash_map = {}
    for integer in a:
        if integer in hash_map:
            hash_map[integer] += 1
        else:
            hash_map[integer] = 1
    for key, value in hash_map.items():
        if value == 1:
            return key
    # More optimal solution (O(n)):
    # return  2 *(sum(set(a))) - sum(a) 

if __name__ == '__main__':
    a  = [1,2,3,4,3,2,1,5,4]
    print(lonelyinteger(a))
    print(set(a))
    print(sum(a))
    print(sum(set(a)))