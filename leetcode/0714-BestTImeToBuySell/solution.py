from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = [0]*len(prices) # hold[i] is the max profit at day i when holding a stock
        unhold = [0]*len(prices) # unhold[i] is the max profit at day i when not holding a stock
        hold[0] = -prices[0]
        for i in range(1,len(prices)):
            hold[i] = max(hold[i-1], unhold[i-1]-prices[i]) # this is the max of holding a stock at day i
            unhold[i] = max(unhold[i-1], hold[i-1]+prices[i]-fee) # this is the max of not holding a stock at day i
        return unhold[-1]

# time: O(n), space: O(n) for hold and unhold array

test = Solution()
print(test.maxProfit([1,3,2,8,4,9],2)) # 8
        