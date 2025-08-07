from collections import Counter

def checkPermutation(s1: str, s2: str) -> bool:
    # problem: check if two strings are permutations of each other
    # my solution: create hashmap that counts occurences of chars in both strings, compare
    # time: O(n), space: O(n)
    if s1 == s2:
        return True

    # simpler with Counter
    # return Counter(s1) == Counter(s2)

    # if can't use Counter
    s1_map = {}
    s2_map = {}
    for s in s1:
        if s in s1_map:
            s1_map[s]+=1
        else:    
            s1_map[s] = 1
    for s in s2:
        if s in s2_map:
            s2_map[s]+=1
        else:    
            s2_map[s] = 1

    if s1_map == s2_map:
        return True
    else:
        return False
    


def testCase(s1:str, s2: str, expected: bool):
    print(s1, s2)
    print(f'Got: {checkPermutation(s1, s2)}, expected: {expected}')

testCase("sadf", "asdf", True)
testCase("kayak", "yakak", True)
testCase("jj", "kk", False)
    

