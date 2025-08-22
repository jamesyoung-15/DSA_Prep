from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """  
        Scan boundaries of rectangle by finding: 
        - min row that contains 1 for top boundary
        - max row that contains 1 for bottom boundary
        - min col that contains 1 for left boundary
        - max col that contains 1 for right boundary
        Create area from boundary

        time: O(n*m), where n is row, m is col
        space: O(1)
        """
        n, m = len(grid), len(grid[0]) # len of row, col
        top, bottom, left, right = n,0,m,0
        
        for row_idx in range(n):
            for col_idx in range(m):
                if grid[row_idx][col_idx] == 1:
                    top = min(top, row_idx)
                    bottom = max(bottom, row_idx)
                    left = min(left, col_idx)
                    right = max(right, col_idx)
        if top == n: top = 0
        if left == m: left = 0  
        area = (bottom - top + 1) * (right - left + 1)
        return area