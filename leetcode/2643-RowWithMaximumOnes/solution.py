class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = 0
        max_sum = 0
        curr_row = 0


        for row in mat:
            curr_sum = sum(row)
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_row = curr_row
            curr_row += 1
        
        return [max_row, max_sum]