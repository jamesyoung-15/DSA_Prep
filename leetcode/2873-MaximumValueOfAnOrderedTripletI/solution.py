class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # greedy + prefix approach: track max nums[i] seens, at index j compute max diff (nuims[i] - nums[j]), at index k update max result
        # time: O(n), space: O(1)

        # n = len(nums)
        # max_result = 0 # to keep track of the maximum product of max_difference and the current number
        # max_number = 0 # store max value encountered so far
        # max_difference = 0 # store max difference between max number and other number

        # for i in range(1,n):
        #     # use current number as nums[k]
        #     max_result = max(max_result, max_difference * num)

        #     # use current number as nums[j]
        #     max_number = max(max_number, num)

        #     # for nums[i] in future calculations
        #     max_difference = max(max_difference, max_number - num)

        # return max_result

        # less optimal: greedy approach of finding current max nums[i] then finding j and k combo
        # time: O(n^2), space: O(1)

        n = len(nums)
        left = nums[0]
        result = 0
        for j in range(n):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j+1,n):
                result = max(result, (left-nums[j])*nums[k])

        return result