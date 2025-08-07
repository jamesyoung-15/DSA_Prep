from collections import defaultdict

def oneAway(str1:str, str2:str) -> bool:
    # problem: 3 edit types (insert, remove, replace), given two strings check if they are one edit away
    # solution: using hashmaps check number of differences (either length of diff in chars), must be < 0
    # time: O(n), space: O(n)
    n, m = len(str1), len(str2)
    if abs(n-m) > 1:
        return False
    
    str1_map = defaultdict(int)
    str2_map = defaultdict(int)
    
    for char in str1:
        str1_map[char] += 1
    for char in str2:
        str2_map[char] += 1
    
    def checkDifferences(longer_map:defaultdict, map2:defaultdict):
        num_diff = 0
        for char, occur in longer_map.items():
            # if char doesn't exist or has more/less occurences, increment num diff
            if char not in map2 or map2[char] != longer_map[char]:
                num_diff += 1
        return num_diff

    num_diff = 0
    if n > m:
        num_diff = checkDifferences(str1_map, str2_map)
    else:
        num_diff = checkDifferences(str2_map, str1_map)
    
    if num_diff > 1:
        return False
    else:
        return True

def test(str1, str2, expected):
    print(f"Input: {str1} and {str2}, Output: {oneAway(str1, str2)}, Expected {expected}")



test("pale", "ple", True)
test("pales", "pale", True)
test("pale", "bale", True)
test("pale", "bake", False)
test("pales", "ple", False)
test("James", "ames", True)
test("palea", "palle", False)