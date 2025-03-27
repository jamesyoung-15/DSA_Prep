class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # sum x moves and y moves, should be 0 for both if true
        # time: O(n), space: O(1)
        y_directions, y_score = {'U':1, 'D':-1}, 0
        x_directions, x_score = {'L':-1, 'R':1}, 0

        for move in moves:
            if move in x_directions:
                x_score += x_directions[move]
            elif move in y_directions:
                y_score += y_directions[move]
        
        return x_score == 0 and y_score == 0