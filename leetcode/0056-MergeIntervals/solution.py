from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first sort by starting intervals
        intervals.sort(key=lambda x:x[0])
        # add the first interval to stack
        stack = [intervals[0]]
        for i in range(1,len(intervals)):
            # compare the top of stack to next interval in intervals, eg. [1,3] vs [2,6] in [[1,3],[2,6],[8,10]] in first loop
            prev = stack[-1]
            current = intervals[i]
            # print(prev, current)
            # compare the previous ending interval vs the next interval start, eg. 3 vs 2 in [1,3] vs [2,6] 
            # if next start is smaller than previous end then update previous end to the max of previous and current ending interval. Eg. [1,3] vs [2,6], 2<3 so update 3 -> max(3,6)
            if current[0] <= prev[1]:
                prev[1] = current[1]
            else:
                stack.append(current)
        return stack

# time: O(nlogn), space: O(n)
intervals = [[1,3],[2,6],[8,10],[15,18]]
test = Solution().merge(intervals)
print(test)