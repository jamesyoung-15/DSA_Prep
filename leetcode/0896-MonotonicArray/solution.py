from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # check if we should be looking for increase (1) or decrease (2), 0 for uninitialized
        checker = 0
        
        for i in range(len(nums)-1):
            # update checker
            if checker == 0:
                if nums[i] > nums[i+1]:
                    checker = 2
                elif nums[i]<nums[i+1]:
                    checker = 1

            # should be decreasing but is increasing
            if checker == 2 and nums[i] < nums[i+1]:
                return False
            # should be increasing but is decreasing
            elif checker == 1 and nums[i] > nums[i+1]:
                return False
        return True

# time: O(n), memory: O(1)

print(Solution().isMonotonic([1,3,2]))