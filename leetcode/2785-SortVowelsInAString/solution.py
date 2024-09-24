class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        hash_map = {char: 0 for char in vowels}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
        print(hash_map)

        result = ""
        sorted_vowel_index = 0
        for char in s:
            if char not in vowels:
                result += char
            else:
                for i in range(len(vowels)):
                    num_vowel = hash_map[vowels[sorted_vowel_index]]
                    if num_vowel == 0:
                        sorted_vowel_index+=1
                    else:
                        break
                result += vowels[sorted_vowel_index]
                hash_map[vowels[sorted_vowel_index]] -= 1
                
        return result