from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start from bottom left
        m,n = len(matrix), len(matrix[0])
        row, col = m-1, 0
        # if current value is less than target, move up a row, otherwise move right a column
        while row>=0 and col<n:
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr > target:
                row-=1
            elif curr < target:
                col+=1

        return False