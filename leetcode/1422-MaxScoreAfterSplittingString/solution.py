class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        # count number of ones
        for char in s:
            if char == '1':
                ones += 1
        
        score = 0
        counter = 0
        # increasing left side, update score as we go
        for char in s:
            if counter == len(s)-1:
                break
            counter+=1
            if char == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(score, ones+zeros)
        return score