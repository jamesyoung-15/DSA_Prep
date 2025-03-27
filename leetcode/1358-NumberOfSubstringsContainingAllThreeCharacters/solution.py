class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # solution: sliding window
        # time complexity: O(n), space complexity: O(1)
        result = 0
        left = 0
        char_count = defaultdict(int)
        for right in range(len(s)):
            char_count[s[right]] += 1

            while len(char_count) == 3:
                result += (len(s) - right)
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0: char_count.pop(s[left])
                left += 1


        return result