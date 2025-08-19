class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        """ 
        Approach:
        Use prefix sums and sliding window technique to calculate the maximum profit.

        Time: O(n) - 3 passes through the prices list
        Space: O(n) - for the prefix sums arrays  
        """
        n = len(prices)
        original_profit = sum(prices[i] * strategy[i] for i in range(n))
        
        if k > n or k == 0:
            return original_profit
        
        half_k = k // 2
        
        hold_diff = [0] * n
        sell_diff = [0] * n 
        
        for i in range(n):
            hold_diff[i] = -strategy[i] * prices[i]
            sell_diff[i] = (1 - strategy[i]) * prices[i]
        
        hold_prefix = [0] * (n + 1)
        sell_prefix = [0] * (n + 1)
        
        for i in range(n):
            hold_prefix[i + 1] = hold_prefix[i] + hold_diff[i]
            sell_prefix[i + 1] = sell_prefix[i] + sell_diff[i]
        
        max_profit_diff = 0
        
        for start in range(n - k + 1):
            hold_sum = hold_prefix[start + half_k] - hold_prefix[start]
            sell_sum = sell_prefix[start + k] - sell_prefix[start + half_k]
            
            profit_diff = hold_sum + sell_sum
            max_profit_diff = max(max_profit_diff, profit_diff)
        
        return original_profit + max_profit_diff