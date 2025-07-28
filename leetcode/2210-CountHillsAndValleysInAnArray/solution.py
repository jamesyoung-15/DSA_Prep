from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """ 
        Two pointer kind of solution, each time process 3 adjacent points, check if hill or valley
        Use separate left_ptr as we need to process last two points as well

        Time: O(n)
        Space: O(1)
        """
        result = 0
        left_ptr = 0
        for i in range(1, len(nums)-1):
            middle = nums[i]
            right = nums[i+1]
            left = nums[left_ptr]
            if middle == right:
                continue
            # hill
            if (middle > left and middle > right):
                result += 1
            # valley
            if (middle < left and middle < right):
                result+=1
            left_ptr = i

        
        return result
            