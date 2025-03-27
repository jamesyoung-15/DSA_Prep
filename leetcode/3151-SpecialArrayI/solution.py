class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # 0 indicates even, 1 indicates odd
        prev = -1 
        for curr in nums:
            if curr%2==0 and prev == 0:
                return False
            if curr%2==1 and prev == 1:
                return False
            if curr%2 == 0:
                prev = 0
            else:
                prev = 1
        return True