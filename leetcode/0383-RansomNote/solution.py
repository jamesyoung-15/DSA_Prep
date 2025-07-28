class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        letters = [0] * 26
        for char in magazine:
            letters[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            if letters[ord(char) - ord('a')] == 0:
                return False
            letters[ord(char) - ord('a')] -= 1
        
        return True