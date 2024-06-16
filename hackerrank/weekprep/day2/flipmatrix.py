""" 
2n x 2n matrix, goal is to maximize sum of elements in the n x n matrix located in the upper-left quadrant of matrix.

Eg.
Input: matrix = [[1,2],[3,4]]

Next reverse row 1: [[1,2][4,3]]
Next reverse column 0: [[4,2],[1,3]]
Maximal sum is 4

"""

"""
Don't think about flipping the rows and columns... There are too many possible outcomes.

Instead, think about what values you can get into the different places. 
For example, in (0,0) you can get any of the 4 corners. 
Keep that pattern going and you should start to see a pretty simple algorithm present itself. 
https://drive.usercontent.google.com/download?id=1t_7fU2LD06qfyIOiFTJ51X8npx0qmcca&export=view&authuser=0
"""
def flippingMatrix(matrix):
    # Write your code here
    maximal_sum = 0
    n = len(matrix)//2
    # 
    for i in range(n):
        for j in range(n):
            print(i,j)
            print(2*n-1-i, j)
            print(i, 2*n-1-j)
            print(2*n-1-i, 2*n-1-j)
            print()
            maximal_sum += max(matrix[i][j], matrix[2*n-1-i][j], matrix[i][2*n-1-j], matrix[2*n-1-i][2*n-1-j])


    return maximal_sum

if __name__ == '__main__':
    input_matrix = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]
    print(flippingMatrix(input_matrix))

    