from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """ 
        Sliding window approach,
        where we maintain a window that contains at most two types of fruits.
        When window exceeds two types, we shrink it from the left.
        
        time: O(n)
        space: O(1) - dictionary should have max 3 keys
        """
        basket = defaultdict(int)
        left = 0
        max_fruits = 0
        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0: del basket[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right-left+1)
        return max_fruits
