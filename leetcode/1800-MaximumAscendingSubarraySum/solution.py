class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            if i == len(nums)-1:
                break
            if nums[i] >= nums[i+1]:
                curr_sum = 0
        
        return max_sum