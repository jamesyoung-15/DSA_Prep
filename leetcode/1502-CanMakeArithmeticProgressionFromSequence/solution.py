from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)==2:
            return True
        arr.sort()
        diff = abs(arr[0] - arr[1])
        for i in range(len(arr)-1):
            diff2 = abs(arr[i] - arr[i+1])
            if diff2 != diff:
                return False
        return True
    
# time: O(nlogn), memory: O(1)

print(Solution().canMakeArithmeticProgression([3,5,1]))