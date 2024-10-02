class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # add s+s, check if s in s+s from index 1 to len(s)-2
        # eg. s=aa, s+s=aaaa, s+s[1:-1]=aa, so s is true
        combined = s+s
        return s in combined[1:-1]
    

# time: O(n) since concat, memory: O(n) b/c of combined string

test = "aa"
print(Solution().repeatedSubstringPattern(test))