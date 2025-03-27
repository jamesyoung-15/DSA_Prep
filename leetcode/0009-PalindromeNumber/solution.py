class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solution: reverse number and compare with original
        # time: O(log(n)), space: O(1)

        if x<0:
            return False
        # reverse number
        reverse = 0
        temp = x
        while temp > 0:
            reverse = reverse * 10 + (temp % 10)
            temp //= 10
        
        return x == reverse



test_num = -121
test = Solution()
print(test_num, test.isPalindrome(test_num))
test_num = 121
print(test_num, test.isPalindrome(test_num))
