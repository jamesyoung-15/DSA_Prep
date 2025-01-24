class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # two dictionary solution
        # time: O(n), space: O(n)

        # store mappings in each dictionary, for example 1 s dictionary will be (e:a) and t dictionary will be (a:e)
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            # compare stored mappings to actual character in the other string's character (ie. s dictionary compare to t character), if mismatch return false
            s_char, t_char = s[i],t[i]
            if s_char in s_dict and s_dict[s_char] != t_char:
                return False
            if t_char in t_dict and t_dict[t_char] != s_char:
                return False
            # add mappings
            s_dict[s_char] = t_char
            t_dict[t_char] = s_char

        return True