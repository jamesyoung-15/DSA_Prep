class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # use set, return on first repeated letter
        # time: O(n), space: O(n)
        seen = set()
        for char in s:
            if char in seen:
                return char
            else:
                seen.add(char)
        