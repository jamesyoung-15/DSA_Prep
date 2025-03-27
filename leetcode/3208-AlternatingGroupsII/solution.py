from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # solution: extend colors list to twice its length, then use sliding window
        # time: O(n), space: O(n)

        extended_colors = [0] * len(colors) * 2
        for i in range(len(colors)):
            extended_colors[i], extended_colors[i+len(colors)] = colors[i], colors[i]

        left = 0
        result = 0
        for right in range(len(colors)+k-1):
            if right > 0 and extended_colors[right] == extended_colors[right-1]:
                left = right
            if right-left+1 > k:
                left += 1
            if right-left+1 == k:
                result += 1

        return result