import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary = '{:032b}'.format(n)
    result = 0
    power = 31
    for bit in binary:
        print(bit)
        if int(bit) == 0:
            result += math.pow(2, power)
        power -= 1
    
    # return unsigned decimal integer result
    return int(result)

if __name__ == '__main__':
    n = int(1)
    result = flippingBits(n)
    print(result)