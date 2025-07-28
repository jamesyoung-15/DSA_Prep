class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) > max_diff:
                max_diff = abs(nums[i] - nums[i+1])
        
        if abs(nums[-1] - nums[0]) > max_diff:
            max_diff = abs(nums[-1] - nums[0])
        return max_diff