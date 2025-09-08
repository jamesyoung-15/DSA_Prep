class Solution:
    def sumZero(self, n: int) -> List[int]:
        """  
        Approach:
        Use two pointers, fill array from both ends to create a symmetric array.
        For odd n, the middle element will be 0 by default.

        time: O(n)
        space: O(1) - not considering output array
        """
        result = [0] * n
        left, right = 0, n-1
        i = 1
        while left<right:
            result[left] = -i
            result[right] = i
            i+=1
            left+=1
            right-=1

        return result