from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # go through possible piles, use binary search
        # time: O(nlog(k)), space: O(1)

        total_c = sum(candies)
        if total_c < k:
            return 0
        
        result = 0
        min_c, max_c = 1, total_c // k

        while min_c <= max_c:
            mid_c = (max_c + min_c) // 2
            num_groups = 0
            for c in candies:
                if c >= mid_c:
                    num_groups += (c // mid_c)
                if num_groups >= k:
                    break
            if num_groups >= k:
                result = mid_c
                min_c = mid_c + 1
            else:
                max_c = mid_c - 1
        return result