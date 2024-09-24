from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # hashmap to store number:frequency
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        # sort the hashmap:
        # first sort by key from largest to smallest to so that in cases where frequency are same it will be sorted from larger to smaller
        # then sort by value from smallest to greatest to sort by frequency
        hash_map = dict(sorted(hash_map.items(),reverse=True))
        sorted_keys = list(sorted(hash_map, key=lambda i:hash_map[i]))

        # print(hash_map)

        final_arr = []
        for key in sorted_keys:
            freq = hash_map[key]
            for i in range(freq):
                final_arr.append(key)
        return final_arr


test_nums = [2,3,1,3,2]
test_nums = [-1,1,-6,4,5,-6,1,4,1]

test_sol = Solution().frequencySort(test_nums)

print(test_sol)