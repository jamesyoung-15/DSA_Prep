class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        
        for char in s:
            if char in hashmap: hashmap[char] += 1
            else: hashmap[char] = 1
        
        a1 = 0 # max odd
        a2 = 1000 # min even
        for char, occurences in hashmap.items():
            if occurences % 2 != 0 and occurences > a1: a1 = occurences
            if occurences % 2 == 0 and occurences < a2: a2 = occurences
        return a1 - a2
