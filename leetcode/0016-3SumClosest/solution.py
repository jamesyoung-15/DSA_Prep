class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # solution: similar to 3sum problem, fix one number and perform binary search to find other two numbers, but this time add check to update closest to target as well
        # time: O(n^2), space: O(1)

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            # skip dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == target:
                    return target
                # update closest
                if abs(target-cur_sum) < abs(target-result):
                    result = cur_sum
                # binary search part
                if cur_sum > target:
                    right-=1
                else:
                    left+=1
        return result