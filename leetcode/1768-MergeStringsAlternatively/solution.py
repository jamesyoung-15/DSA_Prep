class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        # if equal, simply append
        if len(word1) == len(word2):
            for i in range(len(word1)):
                result += word1[i] + word2[i]
        # if unequal, append both first, then append remainder of longer word
        elif len(word1)>len(word2):
            for i in range(len(word2)):
                result += word1[i] + word2[i]
            result+=word1[len(word2):]
        elif len(word2)>len(word1):
            for i in range(len(word1)):
                result += word1[i] + word2[i]
            result+=word2[len(word1):]
        return result

word1, word2 = "ab" , "pqrs"

print(Solution().mergeAlternately(word1,word2))