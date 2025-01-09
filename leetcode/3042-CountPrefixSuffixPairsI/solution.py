class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # brute force solution, compare each string to each other
        # time: O(n^2*L), where n is number of words and L is length of string
        # space: O(1)

        result = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                word1, word2 = words[i], words[j]
                word1_length = len(word1)
                # check prefix and suffix
                if word1 == word2[:word1_length] and word1 == word2[-word1_length:]:
                    result += 1
        
        return result
