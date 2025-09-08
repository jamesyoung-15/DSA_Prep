from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """ 
        Approach:
        Start from a = 1, b = n-1 and check if both a and b contain '0'.
        If any of them contains '0', increment a by 1 and decrement b by 1.
        Repeat until both a and b do not contain '0'.

        time: O(nlogn), in Python int to str conversion takes O(logn)
        space: O(1)
        """
        
        a = 1
        b = n-a

        while '0' in str(a) or '0' in str(b):
            a += 1
            b = n-a

        return [a,b]