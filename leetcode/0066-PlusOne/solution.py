from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig_sum = 0
        exp = len(digits) - 1
        for i in range(len(digits)):
            dig_sum += (digits[i] * 10**exp)
            exp-=1
        dig_sum += 1
        dig_sum = str(dig_sum)
        result = []
        for num in dig_sum:
            result.append(int(num))
        return result

# time: O(n), memory: O(n)
