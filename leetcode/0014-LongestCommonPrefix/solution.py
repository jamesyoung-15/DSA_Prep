class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find min string index and length
        minimum_string_length, minimum_string_index = len(strs[0]), 0
        for idx, string in enumerate(strs):
            if minimum_string_length > len(string):
                minimum_string_length, minimum_string_index = len(string),idx
        
        # compare each string, update longest common prefix by incrementing until we either have difference in prefix or we reach the length of minimum length of string in string list
        # longest_common_prefix = ""
        reference_string = strs[minimum_string_index]
        i = 0
        while i < minimum_string_length:
            for string in strs:
                if string[i] != reference_string[i]:
                    return reference_string[:i]
            i+=1
        
        return reference_string[:i]

