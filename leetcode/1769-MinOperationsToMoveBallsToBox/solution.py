class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # brute force, time: O(n^2), space: O(n)
        output = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                elif boxes[j] == "1":
                    moves += abs(i-j)
            output.append(moves)
        return output