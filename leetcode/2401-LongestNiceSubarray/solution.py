class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        bitmask = 0
        result = 1
        for right in range(len(nums)):
            while bitmask & nums[right] != 0:
                bitmask ^= nums[left]
                left+=1
            
            bitmask = bitmask | nums[right]
            result = max(result, right-left+1)

        return result