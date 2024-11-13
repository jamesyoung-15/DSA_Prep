from typing import Optional, List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # using two pointer
        left, right = 0, len(height)-1
        area = 0
        while left<=right:
            # calculate area
            width = right - left
            curr_height = min(height[left], height[right])
            curr_area = width * curr_height
            area = max(area, curr_area)

            # move left pointer if its height is smaller, move right otherwise
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return area
            