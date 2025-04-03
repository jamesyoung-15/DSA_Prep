class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """ 
        Use a dictionary to store elements as key and index as value.
        Loop through list, find difference between target and element check if      
        difference already exists in hash_map and if it does return the solution 
        otherwise create entry in hashmap 
        """

        hash_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map:
                return [hash_map[difference],i]
            else:
                hash_map[nums[i]] = i

nums = [2,7,11,15]
target = 9
test = Solution().twoSum(nums,target)
print(test)