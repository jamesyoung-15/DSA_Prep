class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        output = [0] * len(nums)


        for i in range(len(nums)):
            left_sum += nums[i]
            output[i] = abs(left_sum - right_sum)
            right_sum -= nums[i]
        return output