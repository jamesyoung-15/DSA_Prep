from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Approach:
        Use a dictionary to store the elements of each diagonal.
        Elements in same diagonal have the same sum of indices (i + j). 
        If the key is even, we will reverse the order of the elements before adding them to the result.

        time: O(m * n)
        space: O(m * n) 
        """
        result = []
        if not mat: return result
        lines = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lines[i+j].append(mat[i][j])
        for key, val in lines.items():
            if key % 2 == 0:
                result += val[::-1]
            else:
                result += val
        return result