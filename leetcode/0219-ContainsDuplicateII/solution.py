class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # build dictionary of num:index
        # iterate through nums, find duplicate nums and check if indices satisfy k condition

        my_dict = {}
        for idx,num in enumerate(nums):
            if num in my_dict and abs(my_dict[num] - idx) <= k:
                # print(my_dict[num], idx,num )
                return True
            my_dict[num] = idx

        return False