class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# time: O(n), space: O(n)

print(Solution().lengthOfLastWord("Hello World"))