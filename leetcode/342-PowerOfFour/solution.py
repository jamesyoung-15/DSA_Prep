class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """ 
        Approach:
        We will use a while loop to divide n by 4 as long as it is divisible by 4.
        If we end up with 1, then n is a power of 4.

        time: O(log n)
        space: O(1)
        """
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n //= 4
        
        return n == 1