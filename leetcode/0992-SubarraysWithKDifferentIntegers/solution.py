from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            count = defaultdict(int)
            result = 0
            left = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                if count[nums[right]] == 1:
                    k -= 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k+=1
                    left += 1
                result += (right-left+1)
            return result
        return atMostK(k) - atMostK(k-1)