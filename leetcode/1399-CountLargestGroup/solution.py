from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # use dictionary with digit sum as key and occurence of the sum as value
        # iterate from 1 to n and fill dictionary, get max size, then get how many groups match the largest size
        # time: O(n), space: O(n)

        groups = defaultdict(int) # key = sum, value = group size
        # go through each number from 1 to n
        for i in range(1, n+1):
            sum_digits = 0
            # break down integer to digits, sum them
            while i:
                sum_digits += i % 10
                i //= 10
            # add to dictionary
            groups[sum_digits] += 1
        
        # get largest size
        largest_size = max(groups.values())
        num_largest_size = 0
        # count how many groups with largest size
        for group, size in groups.items():
            if size == largest_size:
                num_largest_size += 1
        return num_largest_size