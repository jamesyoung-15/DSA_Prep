class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """ 
        Do as problem says, nothing difficult
        
        time: O(n*m) - not 100% sure, but n being len of sentence and m being max word len
        space: O(n)
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = []
        words = sentence.split()


        for idx, word in enumerate(words):
            num_a = "a" * (idx+1)
            new_word = ""
            if word[0].lower() not in vowels: 
                new_word = (word[1:] + word[0] + "ma")
            elif word[0].lower() in vowels: 
                new_word += (word + "ma")
            new_word += num_a
            result.append(new_word)
            if idx != len(words)-1: result.append(" ")



        return ''.join(result)
