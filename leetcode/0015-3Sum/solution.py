from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time: O(n^2), space: O(1)
        # solution: sort the array, iterate through the array and for each number, use two pointers to find the other two numbers

        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n):
            start_num = nums[i]
            # if positive, since sorted it means that all next numbers are positive so cannot sum to 0
            if nums[i] > 0:
                break
            # skip dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while left<right:
                total = nums[left] + nums[right] + start_num
                if total == 0:
                    answer.append([start_num, nums[left], nums[right]])
                    left, right = left+1, right-1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
                elif total > 0:
                    right-=1
                elif total < 0:
                    left += 1



        return answer

        # nums.sort()
        # answer = set()
        # for i in range(len(nums)-1):
        #     current = -nums[i]
        #     seen = {}
        #     for j in range(i+1,len(nums)):
        #         target = current - nums[j]
        #         if target in seen:
        #             answer.add((nums[i], nums[j], target))
        #         else:
        #             seen[nums[j]] = 1
        # return answer
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))