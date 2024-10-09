from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        # binary search to find if there is a row that is within target range
        low, high = 0, num_rows - 1
        target_row = 0
        while low<=high:
            mid_row = low + (high-low)//2
            target_row = mid_row
            if target>matrix[mid_row][-1]:
                low = mid_row + 1
            elif target<matrix[mid_row][0]:
                high = mid_row - 1
            else:
                break
        # if none of rows are within range, return false
        if low>high:
            return False
        
        # binary search to find if the value exist in the row that the target falls within range
        left, right = 0, num_cols - 1
        while left<=right:
            mid = left + (right-left)//2
            x = matrix[target_row][mid]
            if target == x:
                return True
            elif target>x:
                left = mid + 1
            elif target<x:
                right = mid - 1
        return False
