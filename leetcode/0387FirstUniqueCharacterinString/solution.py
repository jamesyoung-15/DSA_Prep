class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create dictionary, map char:idx, if duplicate exists set value idx to -1
        char_dict = {}
        for idx, char in enumerate(s):
            if char in char_dict:
                char_dict[char] = -1
            else:
                char_dict[char] = idx
        # iterate through dictionary, if value is -1 it means there was duplicate and skip, otherwise return the first key:val where val is not -1
        index = -1
        for key, idx in char_dict.items():
            if idx == -1:
                continue
            else:
                index = idx
                # terminate cause we only want first unique char
                break

        return index


s = "leetcode" # expected 0 cause l is first unique
print(Solution().firstUniqChar(s))

s = "aabb" # expected -1
print(Solution().firstUniqChar(s))