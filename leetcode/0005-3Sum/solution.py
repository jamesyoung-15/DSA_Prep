from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i in range(len(nums)-1):
            current = -nums[i]
            seen = {}
            for j in range(i+1,len(nums)):
                target = current - nums[j]
                if target in seen:
                    answer.add((nums[i], nums[j], target))
                else:
                    seen[nums[j]] = 1
        return answer
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))