# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # bitwise shift left first, then do bitwise OR to least significant bit. 
        # Eg. ans = 5 (101) and curr.val = 1, then bitwise shift makes ans = 10 (1010) and bitwise OR makes ans = 11 (1011)
        # time: O(n), space: O(1)
        answer = 0
        curr = head
        while curr:
            answer = (answer << 1) | curr.val
            curr = curr.next
        return answer
        
