class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # compare each word
        # time: O(n*m), not sure
        # space: O(n)

        # first convert sentence to array, split by space
        sentence_arr = sentence.split(' ')

        # go through array, compare each word to searchWord
        for idx,word in enumerate(sentence_arr):
            # skip if current word smaller than searchWord
            if len(searchWord)>len(word):
                continue
            if word[:len(searchWord)] == searchWord:
                return idx+1
        return -1