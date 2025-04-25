from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative approach: reverse the linked list in place
        # time: O(n), space: O(1)
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
    
        # recursive approach: reverse the linked list recursively by breaking it down into smaller problems
        # if not head or not head.next:
            # return head
        # reverse the rest of the list
        # new_head = self.reverseList(head.next)
        # point the next node to head
        # head.next.next = head
        # head.next = None
        # return new_head


# time: O(n), space: O(1)

ls = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
actual = Solution().reverseList(ls)
curr = actual
print("Original: [0,1,2,3]")
print("Reversed: ")
while curr:
    print(curr.val)
    curr = curr.next
    
