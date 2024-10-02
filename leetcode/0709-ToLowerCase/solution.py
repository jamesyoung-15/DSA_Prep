class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_str = ""
        for char in s:
            if char.isupper():
                lower_str += char.lower()
            else:
                lower_str += char
        return lower_str
# Time: O(n), Space: O(n)
print(Solution().toLowerCase("Hello"))