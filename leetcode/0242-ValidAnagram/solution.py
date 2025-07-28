class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)
        for i in s:
            hash_map[i] += 1
        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
                if hash_map[char] == 0:
                    del hash_map[char]
            else:
                return False
        return not hash_map