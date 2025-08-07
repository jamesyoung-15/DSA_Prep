from collections import Counter

def isPalindromePermutation(s1: str):
    s1_map = Counter(s1)
    num_odd = 0

    for _, occur in s1_map.items():
        if occur%2!=0:
            num_odd+=1
        if num_odd>1:
            return False
    
    return True

print(isPalindromePermutation("abc"))
print(isPalindromePermutation("abaa"))
print(isPalindromePermutation("aabaa"))
print(isPalindromePermutation("aaaadbcbdaaaa"))