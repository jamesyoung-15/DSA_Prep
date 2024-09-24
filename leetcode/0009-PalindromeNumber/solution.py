class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        return int(str(x)[::-1]) == x



test_num = -121
test = Solution()
print(test_num, test.isPalindrome(test_num))
test_num = 121
print(test_num, test.isPalindrome(test_num))
