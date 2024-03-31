""" 
Increasing Array

You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x1,x2,...,x_n: the contents of the array.
Output
Print the minimum number of moves.
Constraints

1 <= n <= 2 * 10^5
1 <= x_i <= 10^9

Example
Input:
5
3 2 5 1 7

Output:
5 
"""

def increasing_array(size, array):
    count = 0
    for i in range(1,size):
        increase = 0
        if array[i] < array[i-1]:
            increase = array[i-1] - array[i]
            array[i] += increase
            count += increase
    return count

if __name__ == '__main__':
    size = int(input())
    array = [int(x) for x in input().split()]
    print(increasing_array(size, array))