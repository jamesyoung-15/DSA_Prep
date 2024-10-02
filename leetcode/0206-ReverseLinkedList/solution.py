from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # point the next node to prev, update prev to current, then move current to next
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # return prev as current will be none
        return prev

# time: O(n), space: O(1)

ls = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
actual = Solution().reverseList(ls)
curr = actual
print("Original: [0,1,2,3]")
print("Reversed: ")
while curr:
    print(curr.val)
    curr = curr.next
    
