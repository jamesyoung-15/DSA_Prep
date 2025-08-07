from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ 
        Initialize first row, for every next row pad create temp array that is previous row with 0 on both ends,
        then iterate through temp array and add two numbers to form new row

        eg: prev row: [1,1], temp: [0,1,1,0], new_row -> [0+1, 1+1, 1+0], result = [[1], [1,1], [1,2,1]]

        time: O(n^2), n is num rows
        space: O(n^2), n is num rows, or O(1) if we exclude answer since
        
        """
        if numRows == 0: return []
        triangle = [[1]]
        for i in range(1, numRows):
            temp = [0] + triangle[-1] + [0] # pad 0s
            row = []
            for j in range(len(temp)-1): # sum adjacent elements
                row.append(temp[j] + temp[j+1])
            triangle.append(row)
        return triangle