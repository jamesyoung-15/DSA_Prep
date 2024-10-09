from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # build hashmap that counts occurences of each number
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        result = 0
        result_arr = []
        # if occurence greater than 1, there are duplicates
        for num, occur in hash_map.items():
            result+=1
            result_arr.append(num)
            
        i = 0
        while i < len(nums):
            if i<len(result_arr):
                nums[i] = result_arr[i]
            i+=1
        

        return result

# time: O(n), space: O(n)
