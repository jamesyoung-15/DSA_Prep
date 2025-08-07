from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """ 
        Brute force approach:
        For each fruit, go through baskets left to right until either a basket is found or all baskets are checked.

        time: O(n*m), n= len(fruits), m=len(baskets)
        space: O(1) - no extra space used
        """
        
        result = len(baskets)
        for fruit in fruits:
            for idx, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[idx] = 0
                    result = max(result-1,0)
                    break
        
        return result