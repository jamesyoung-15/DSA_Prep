from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # index represents 0,1,2, values represent occurences
        occurences = [0,0,0]

        for num in nums:
            occurences[num] += 1

        for i in range(len(occurences)):
            for j in range(occurences[i]):
                nums[i] = i

        # merge sort method
        # if len(nums)>1:
        #     midpoint = len(nums) // 2
        #     left_arr = nums[:midpoint]
        #     right_arr = nums[midpoint:]

        #     self.sortColors(left_arr)
        #     self.sortColors(right_arr)

        #     i, j, k = 0,0,0 # left, right, result

        #     while i<len(left_arr) and j<len(right_arr):
        #         if left_arr[i] <= right_arr[j]:
        #             nums[k] = left_arr[i]
        #             i+=1
        #         else:
        #             nums[k] = right_arr[j]
        #             j+=1
        #         k+=1
        #     # leftovers
        #     while i<len(left_arr):
        #         nums[k] = left_arr[i]
        #         i+=1
        #         k+=1
        #     while j<len(right_arr):
        #         nums[k] = right_arr[j]
        #         j+=1
        #         k+=1


# time: O(n), complexity: O(n)
nums = [1,0,1,2]
print("In: ", nums)
test = Solution().sortColors(nums)
print("Out: ",nums)