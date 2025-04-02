class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # solution: 
        # intuition is to keep track of last index of each letter in the string
        # last index of each letter is used to determine the end of a partition
        # if the current index is the last index of the letter, then the partition ends
        # time: O(n), space: O(1)
        last_indices = {letter:index for index, letter in enumerate(s)}
        left, right = 0, 0
        result = []
        for idx, letter in enumerate(s):
            right = max(right, last_indices[letter])
            if idx == right:
                result.append(right-left+1)
                left = idx + 1
        return result