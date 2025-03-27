def solution(word: str):
    # problem: determine if a string has all unique characters
    # solution: create array of boolean values, one for each character
    # time complexity: O(n), space complexity: O(1)

    # assume ascii, so 128 unique characters
    if len(word) > 128:
        return False
    char_set = [False] * 128
    for char in word:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True


print(solution("abc")) # True
print(solution("aAbBcC")) # True
print(solution("aAbBcC1")) # True
print(solution("AaaBbbasdf")) # False