from collections import defaultdict
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # create dictionary with number:occurence, all numbers must occur even times
        # time: O(n), space: O(n)
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        for num, occur in hashmap.items():
            if occur % 2 != 0:
                return False
        
        return True