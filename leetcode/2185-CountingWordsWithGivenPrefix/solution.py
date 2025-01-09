class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # brute force solution: for each word, compare word[:pref] to pref 
        # time: O(n*k), where n is number of words and k is prefix length
        # space: O(1), don't use word[:prefix_length] otherwise it becomes O(k) space

        number_prefixes = 0
        prefix_length = len(pref)
        for word in words:
            # O(1) space implementation, compare each char in word to prefix
            if len(word)<len(pref):
                continue
            is_pref = 1 # 1 if is prefix, 0 otherwise
            for i in range(prefix_length):
                if word[i] != pref[i]:
                    is_pref = 0
            number_prefixes += is_pref

            # below uses O(k) space
            # if word[:prefix_length] == pref:
                # number_prefixes += 1
        
        return number_prefixes