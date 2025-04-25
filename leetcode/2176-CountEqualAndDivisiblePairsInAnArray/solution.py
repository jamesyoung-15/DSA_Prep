from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # brute force
        # time: O(n^2), space: O(1)
        # result = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if (i*j)%k == 0 and nums[i] == nums[j]:
        #             result+=1
        
        # return result

        # hashmap
        # time: O(n^2) but more efficient, space: O(n)

        hashmap = defaultdict(list)
        result = 0
        for idx, num in enumerate(nums):
            for num2, idx2 in enumerate(hashmap[num]):
                if (idx * idx2)%k == 0:
                    result += 1
            hashmap[num].append(idx)
        return result