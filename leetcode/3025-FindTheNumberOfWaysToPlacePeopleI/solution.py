class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """  
        Approach:
        Sort points by x ascending, and by y descending for same x.
        For each point, iterate through the rest of the points to find valid pairs.
        A valid pair is when the second point's y is less than or equal to the first
        point's y, and greater than any previously found second point's y for the
        current first point.

        time: O(n^2)
        space: O(1) - not considering input storage
        """
        num_pairs = 0
        points.sort(key=lambda x : (x[0], -x[1]))
        for i in range(len(points)):
            _, upper_y = points[i]
            lower_y_limit = -1
            for j in range(i+1, len(points)):
                _, curr_y = points[j]
                if curr_y <= upper_y and curr_y > lower_y_limit:
                    num_pairs += 1
                    lower_y_limit = curr_y
        return num_pairs