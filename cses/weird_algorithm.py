""" 
Weird Algorithm

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. 
The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3->10->5->16->8->4->2->1
Your task is to simulate the execution of the algorithm for a given value of n.
Input
The only input line contains an integer n.
Output
Print a line that contains all values of n during the algorithm.
Constraints

1 <= n <= 10^6

Example
Input:
3

Output:
3 10 5 16 8 4 2 1

"""

def weird_algorithm(n):
    # if even, divide by two
    print(str(n), end=' ')
    if n == 1:
        return
    if n%2 == 0:
        weird_algorithm(n//2)
    else:
        weird_algorithm(n*3+1) 

if __name__ == '__main__':
    problem_input = int(input())
    weird_algorithm(problem_input)
    