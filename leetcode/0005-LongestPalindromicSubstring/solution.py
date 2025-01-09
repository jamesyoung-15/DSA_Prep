class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp approach
        ans = ""
        count = 0
        n = len(s)

        dp = [[False]*n for i in range(n)]

        for i in range(n):
            for j in range(n-i):
                k = i+j
                if i == 0:
                    dp[j][k] = True
                elif i == 1:
                    is_palindrome = (s[j] == s[k]) 
                    dp[j][k] = is_palindrome
                else:
                    is_palindrome = (s[j] == s[k] and dp[j+1][k-1])
                    dp[j][k] = is_palindrome
                if dp[j][k] and count < k-j+1:
                    ans = s[j:k+1]
                    count = len(ans)

        return ans