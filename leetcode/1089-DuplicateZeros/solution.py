from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # keep track of where indices of zeros should go as well as the non-zero order, then merge below 
        non_zeros = [] # keep track of non-zeros 
        zero_indices = [] # keep track of indices of zeros and where duplicates should go
        shift_amount = 0
        for idx, num in enumerate(arr):
            if num != 0:
                non_zeros.append(num)
            else:
                zero_indices.append(idx + shift_amount)
                zero_indices.append(idx+1+shift_amount)
                shift_amount += 1
        # merge based on non-zero order and zero indices
        i,j,k = 0,0,0
        while i<len(arr):
            if k<len(zero_indices) and i == zero_indices[k] and zero_indices[k] < len(arr):
                arr[i] = 0
                k+=1
            elif j<len(arr):
                arr[i] = non_zeros[j]
                j+=1
            i+=1
