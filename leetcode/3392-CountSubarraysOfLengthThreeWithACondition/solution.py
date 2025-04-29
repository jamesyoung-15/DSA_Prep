class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # one pass, loop through 0 to n-2, check every 3 elements to see if valid subarray
        # time: O(n), space: O(1)
        result = 0
        for i in range(len(nums)-2):
            if 2*(nums[i] + nums[i+2]) == nums[i+1]:
                result+=1
        
        return result