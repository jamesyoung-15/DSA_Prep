class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 1
        if n == 1: return True
        new_nums = [0] * 2*n
        for idx, num in enumerate(nums):
            new_nums[idx] = num
            new_nums[idx+n] = num
        
        for i in range(1, len(new_nums)):
            if new_nums[i-1] <= new_nums[i]:
                count+=1
            else:
                count = 1
            if count == n:
                return True
        return False