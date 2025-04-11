class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # time: O(n)
        # space: O(n)
        
        # early return if only one row returns original string (example 3)
        if numRows == 1:
            return s
        
        # idea is to fill out top to bottom then bottom to top
        zigzag = [[] for _ in range(numRows)] 
        step = 1 # 1 go down, -1 go up
        current_row = 0
        for char in s:
            zigzag[current_row].append(char)
            # if at top, need to go down
            if current_row == 0:
                step = 1
            # if we reach bottom, turn back up
            elif current_row == numRows - 1:
                step = -1
            current_row+=step
        
        
        answer = ""
        for row in zigzag:
            answer += ''.join(row)
            
        # print(answer)

        return answer