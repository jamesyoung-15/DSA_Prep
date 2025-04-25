class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search to find the index of target, if not found return index where it can be inserted
        # time: O(logn), space: O(1)
        left, right = 0, len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        # after loop, left is the index where target can be inserted
        if left == len(nums)-1 and nums[left] < target:
            return left+1
        return left