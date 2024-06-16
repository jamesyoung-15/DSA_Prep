import math
""" 
1 2 3
4 5 6
9 8 9

The left-to-right diagonal 1+5+9 = 15. The right to left diagonal 3+5+9 = 17. Their absolute difference is |15-17| = 2. 

"""


def diagonalDifference(arr):
    # Write your code here
    left_right_sum = 0
    right_left_sum = 0
    
    # loop through array
    for i in range(len(arr[0])):
        # for left-right, goes like [0][0] -> [1][1] ... -> [n][n], so just use arr[i][i]
        left_right_sum += arr[i][i]
        # for right left, goes like [2][0] -> [1][1] -> [0][2], basically decrement row and increase column
        right_left_sum += arr[len(arr[0]) - 1 - i][i]

        
    result = abs(left_right_sum - right_left_sum)

    return result

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6], [9,8,9]]
    result = diagonalDifference(arr)
    print(result)