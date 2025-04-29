class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window, move right pointer from left to right, if max number occurs >= k times then move left pointer and update result
        # time: O(n), space: O(1)
        max_num = max(nums)
        left = 0
        max_num_occurence = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == max_num:
                max_num_occurence += 1
            while max_num_occurence>=k and left < len(nums):
                if nums[left] == max_num:
                    max_num_occurence -= 1
                left += 1
                result += len(nums) - right

        return result