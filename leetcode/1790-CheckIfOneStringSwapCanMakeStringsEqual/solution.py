class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # solution: use hashmap, count the number of different characters, should be less than 2
        # time: O(n), space: O(1)
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        
        num_diff = 0
        s1_map = {chr(c):0 for c in range(ord('a' ), ord('z')+1)}
        s2_map = {chr(c):0 for c in range(ord('a' ), ord('z')+1)}

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diff += 1
                if num_diff > 2:
                    return False
            s1_map[s1[i]] += 1
            s2_map[s2[i]] += 1
        
        return s1_map == s2_map