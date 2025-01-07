class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        final_max = 0

        for account in accounts:
            curr_sum = sum(account)
            if curr_sum > final_max:
                final_max = curr_sum
        
        return final_max