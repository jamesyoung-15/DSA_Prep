class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a hash set of items I have seen, if there is a repeated char, it will show up in dictionary, then we know to stop and get length
        char_set = set()
        # create start and end pointer to keep track of longest strings
        maxLength, start, end = 0, 0, 0
        while end<len(s):
            # if the character is not in the set, it's a unique character for the current substring, add to hash set and move end
            if s[end] not in char_set:
                char_set.add(s[end])
                maxLength = max(maxLength, end - start + 1)
                end += 1
            else:
                # If we find a repeating character, remove the character at the start pointer and move the start pointer
                char_set.remove(s[start])
                start += 1

        return maxLength
    
s = "abcabcbb"
test = Solution().lengthOfLongestSubstring(s)

print(test)