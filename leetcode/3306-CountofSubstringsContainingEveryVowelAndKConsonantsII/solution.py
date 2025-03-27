class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastK(k):
            vowels = 'aeiou'
            seen_vowels = defaultdict(int)
            non_vowel = 0
            result = 0
            left = 0
            for right in range(len(word)):
                if word[right] in vowels:
                    seen_vowels[word[right]] += 1
                else:
                    non_vowel+=1
                while len(seen_vowels) == 5 and non_vowel >= k:
                    result += (len(word) - right)
                    if word[left] in vowels: seen_vowels[word[left]] -= 1
                    elif word[left] not in vowels: non_vowel -= 1
                    if seen_vowels[word[left]] == 0: seen_vowels.pop(word[left])
                    left+=1
            return result
        
        return atLeastK(k) - atLeastK(k+1)