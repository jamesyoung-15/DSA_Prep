from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product *= i
        # print(product)
        if product>0:
            return 1
        elif product<0:
            return -1
        return 0

# time: O(n), memory: O(1)
print(Solution().arraySign([-1,-2,-3,-4,3,2,1])) # should be 1