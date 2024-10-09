# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pick = 5
    if num == pick:
        return 0
    elif num>pick:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n
        while low<=high:
            mid = low + (high-low)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 1:
                low = mid+1
        return n
    
print(Solution().guessNumber(100))