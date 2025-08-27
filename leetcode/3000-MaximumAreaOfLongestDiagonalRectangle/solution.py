from typing import List
import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """ 
        Calculate diagonal, area for each rectangle and keep track of max diag and area

        Time: O(n)
        Space: O(1)  
        """
        max_diag = 0
        max_area = 0
        for (length, width) in dimensions:
            diag = math.sqrt(length * length + width*width)
            area = length * width
            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif diag == max_diag:
                max_area = max(max_area,area)
            

        return max_area