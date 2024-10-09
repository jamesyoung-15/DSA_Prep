class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_paren = 0
        result = 0
        for paren in s:
            if paren == '(':
                open_paren += 1
            else:
                open_paren -= 1
                if open_paren < 0:
                    open_paren += 1
                    result += 1
        
        return result + open_paren