from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return sqrt(x**2+y**2)
        
        # max-heap solution
        # time complexity: O(nlog(k)), space complexity: O(k)
        heap = []
        for x,y in points:
            distance = dist(x,y)
            if len(heap) < k:
                heapq.heappush(heap, (-distance,x,y))
            else:
                heapq.heappushpop(heap, (-distance,x,y))
        
        return [(x,y) for _,x,y in heap]



        # sort by distance solution: 
        # time complexity: O(nlog(n)), space complexity: O(n)) 
        # points.sort(key=lambda point: dist(point[0],point[1]))

        # return points[:k]