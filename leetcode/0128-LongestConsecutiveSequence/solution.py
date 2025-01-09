class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # solution: use set, check if number in nums is the start of subsequence, count length of that subsequence if it is start
        # time: O(n), space: O(n)

        # create set from nums for O(1) lookup
        nums_set = set(nums)
        longest_subsequence = 0

        # iterate through nums_set instead of nums to skip duplicates, otherwise tle
        for num in nums_set:
            # if num-1 is not in the set, it means that it is start of sequence
            if num-1 not in nums_set:
                next_num = num+1
                length = 1
                # check how long the subsequence is, update if longer than longest subsequence
                while next_num in nums_set:
                    next_num += 1
                    length+=1
                longest_subsequence = max(longest_subsequence, length)
        
        return longest_subsequence
