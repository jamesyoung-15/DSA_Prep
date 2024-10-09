from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles) # range of possible k values
        result = 0
        # use binary search to try different k values
        while low<=high:
            mid = low + (high-low)//2
            # find total hours it would take to eat with k
            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile)/mid)
            # binary search logic
            if total_time<=h:
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
    
print(Solution().minEatingSpeed([3,6,7,11],8)) # expected output: 4