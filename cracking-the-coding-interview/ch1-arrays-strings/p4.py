from collections import defaultdict

def palindromePermutation(input:str) -> bool:
    # problem: check if input has a permutation that is palindrome
    # solution: to be able to form palindrome, it needs match one of two cases:
    # case 1: have only even occurences of each unique char
    # case 2: have only one odd occurence of a unique char
    # time: O(n), space: O(n)

    char_occur = defaultdict(int)
    for char in input:
        char_occur[char] += 1
    
    has_odd_occur = 0
    for char, occur in char_occur.items():
        if occur % 2 != 0:
            has_odd_occur += 1
        if has_odd_occur > 1:
            return False

    return True


def test(input:str, expected:bool):
    print(f"Input: {input},Got: {palindromePermutation(input)}, Expected: {expected}")

test("Tact Coa", True)
test("James", False)
test("kayak", True)
test("yakak", True)