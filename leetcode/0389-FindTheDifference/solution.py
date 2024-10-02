class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # take sum of ascii characters in both s and t, subtract them to find difference and return the ascii character of remainder value
        s_sum = 0
        for char in s:
            s_sum += ord(char)
        t_sum = 0
        for char in t:
            t_sum += ord(char)

        return chr(t_sum - s_sum)
    
# Time: O(n), Memory: O(1)
s, t = "abcd", "aebcd"
test = Solution().findTheDifference(s,t)
print(test)
