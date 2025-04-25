class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # 2 pass solution: find min distance going right and going left
        # time: O(n), space: O(1)

        if words[startIndex] == target:
            return 0

        n = len(words)
        min_dist_right = n
        for i in range(n):
            if words[(startIndex+i)%n] == target: 
                min_dist_right = i 
                break
        
        if min_dist_right == n:
            return -1

        min_dist_left = n
        for i in range(n):
            if words[(startIndex-i)%n] == target: 
                min_dist_left = i 
                break

        return min(min_dist_left, min_dist_right)