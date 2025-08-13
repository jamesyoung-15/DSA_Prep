class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """ 
        Iteratively divide n by 3 until it is no longer divisible.
        If we end up with 1, then n is a power of three.

        Time: O(log n)
        Space: O(1) 
        """
        if n == 1: return True
        elif n < 3: return False

        while n % 3 == 0:
            n //= 3
        return n == 1

def test():
    sol = Solution()
    assert sol.isPowerOfThree(1) == True
    assert sol.isPowerOfThree(3) == True
    assert sol.isPowerOfThree(9) == True
    assert sol.isPowerOfThree(27) == True
    assert sol.isPowerOfThree(0) == False
    assert sol.isPowerOfThree(2) == False
    assert sol.isPowerOfThree(10) == False
    assert sol.isPowerOfThree(28) == False

if __name__ == "__main__":
    test()
    print("All tests passed.")