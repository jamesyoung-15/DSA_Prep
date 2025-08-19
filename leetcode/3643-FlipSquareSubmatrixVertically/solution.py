class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        """  
        Approach:
        We will swap the rows in the submatrix defined by (x, y) and size k.
        Specifically, we will swap the top row with the bottom row, the second row with the second last row, and so on, each time within the boundaries (eg. y to y+k).


        time: O(k^2), since we swap k elements each time so it's k^2
        space: O(1)
        """
        for i in range(k//2):
            row_top, row_bottom = i + x, x + k - 1 - i
            col_start, col_end = y, y+k
            grid[row_top][col_start:col_end], grid[row_bottom][col_start:col_end] = grid[row_bottom][col_start:col_end], grid[row_top][col_start:col_end]
        return grid
        
        