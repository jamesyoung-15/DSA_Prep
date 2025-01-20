from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer solution, time: O(n), space: O(1)
        position_ptr = 0
        for num in nums:
            if num != 0:
                nums[position_ptr] = num
                position_ptr+=1
        
        while position_ptr < len(nums):
            nums[position_ptr] = 0
            position_ptr+=1

        # # create list to keep track of non-zero elements in order
        # non_zeros = []
        # for i,n in enumerate(nums):
        #     if n != 0:
        #         non_zeros.append(n)
        # # count number of zeros
        # number_of_zeros = len(nums) - len(non_zeros)
        # # replace nums[i] with non-zero array, then append number of zeros to end
        # for i in range(len(non_zeros)):
        #     nums[i] = non_zeros[i]
        # nums[len(non_zeros):] = [0]*number_of_zeros