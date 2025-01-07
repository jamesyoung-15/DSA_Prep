class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # solution: create set of unique characters, if set contains 26 unique characters return true else return false
        # time: O(n), space: O(n)
        character_set = set()
        for char in sentence:
            if char not in character_set:
                character_set.add(char)
        
        if len(character_set) == 26:
            return True
        return False
