from collections import defaultdict
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """  
        Approach:
        - Intuition: if x is currently element with least abs value, it must pair with 2*x as there is no other x/2 to pair w/ it
        
        - Greedy solution + hashmap:
          - build frequency counter
          - sort array
          - go through sorted array
            - if current element is already matched, skip
            - if 2*current element is not in hashmap or no more 2*current element to match, return False
            - otherwise pair current element with 2*current element and decrement their counts in hashmap

        Time: O(nlogn) - sorting
        space: O(n) - hashmap and sorted array
        """
        hashmap = defaultdict(int)
        for num in arr: hashmap[num] += 1
        
        arr.sort(key= lambda x: abs(x))
        for idx, num in enumerate(arr):
            # skip if already matched
            if hashmap[num] == 0: continue
            # return false if we don't have 2*num or no more 2*num to match
            if 2*num not in hashmap or hashmap[num*2] == 0: 
                return False
            # match num w/ 2*num
            hashmap[num] -= 1
            hashmap[2*num] -= 1
        return True

def test():
    sol = Solution()
    assert sol.canReorderDoubled([3, 1, 3, 6]) == False
    assert sol.canReorderDoubled([2, 1, 2, 6]) == False
    assert sol.canReorderDoubled([4, -2, 2, -4]) == True
    assert sol.canReorderDoubled([1, 2, 4, 16]) == False
    assert sol.canReorderDoubled([0, 0, 0, 0]) == True
    print("All test cases passed!")

if __name__ == "__main__":
    test()