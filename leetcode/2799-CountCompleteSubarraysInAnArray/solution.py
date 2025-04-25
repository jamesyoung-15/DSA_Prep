class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # sliding window approach, reduce window from left when we reach distinct elements required
        # time: O(n), space: O(n)
        num_uniques = len(set(nums))
        hashmap = defaultdict(int)
        result = 0
        left = 0
        for right in range(len(nums)):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            while len(hashmap) == num_uniques:
                print(left, right)
                result += len(nums) - right
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
                print(left, right)
        
        return result



        # brute force
        # time: O(n^2), space: O(n)
        # unique_nums = set(nums)
        # num_unique = len(unique_nums)
        # result = 0
        # for left in range(len(nums)):
            # set2 = set()
            # for right in range(left, len(nums)):
                # set2.add(nums[right])
                # if len(set2) == num_unique:
                    # result += 1

        # return result