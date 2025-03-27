class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer technique
        # O(n) time and space
        
        new_word = []
        for char in s:
            if char == " ":
                continue
            if not char.isalpha() and not char.isnumeric():
                continue
            if char.isupper():
                new_word.append(char.lower())
            else:
                new_word.append(char)
        
        new_word = ''.join(new_word)
        left, right = 0, len(new_word) - 1
        while left<=right:
            if new_word[left] != new_word[right]:
                # print(left,right)
                return False
            left+=1
            right-=1
        
        return True
