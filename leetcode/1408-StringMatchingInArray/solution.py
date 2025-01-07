from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # solution 1: brute force by comparing each word to every other word
        # time complexity: O(n^2)
        # space complexity: O(n) 

        result = set()

        for i in range(len(words)):
            curr_word = words[i]
            for j in range(len(words)):
                if i == j:
                    continue
                compared_word = words[j]
                if curr_word in compared_word and curr_word not in result:
                    result.add(curr_word)
        
        return list(result)

        # solution 2: combine words into single string, substring of another word will appear twice in the string
        # time: O(n^2)
        # space: O(n)

        # words_string = ' '.join(words)
        # print(words_string)
        # answer = []
        # for word in words:
        #     if words_string.count(word) >= 2:
        #         answer.append(word)
        
        # return answer
        