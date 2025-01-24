class Solution:
    def isHappy(self, n: int) -> bool:
        # set solution: keep track of sum of squares, perform squares and add to set, if next sum is in set and is not 1 then it means it is a cycle and is false
        # time: O(n^2) but not sure, space: O(n)
        seen = set()
        while n not in seen:
            seen.add(n)
            temp_n = n
            while temp_n:
                sum_n += (temp_n%10)**2
                temp_n //= 10
            n = sum_n
        return n == 1

