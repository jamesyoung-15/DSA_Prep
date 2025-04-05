class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # dfs solution
        # time: O(2^n), space: O(n)
        def dfs(i, total):
            if i == len(nums):
                return total
            
            return dfs(i+1,total^nums[i]) + dfs(i+1, total)
        
        return dfs(0,0)