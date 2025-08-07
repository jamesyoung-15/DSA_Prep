class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """ 
        if the minimum element in nums is equal to k, we return (number of unique elements 1).
        otherwise, we return the total number of unique elements
        time: O(n), space: O(n)
        """
        min_num = min(nums)
        if min_num < k:
            return -1
        num_set = set(nums)
        num_unique = len(num_set)
        if min_num == k:
            return num_unique - 1
        else:
            return num_unique
