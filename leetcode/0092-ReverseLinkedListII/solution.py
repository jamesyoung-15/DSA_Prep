from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # go to right before left and store node before left, do normal reverse linked list, then update right before left node to point to after right
        # time: O(n), space: O(1)
    
        if not head.next:
            return head


        head_return = ListNode(0, head) # dummy for returning ll
        # go to right before left
        prev = head_return
        for _ in range(left-1):
            prev = prev.next
        
        left_prev = prev # store node right before left, example1: 1
        curr = prev.next #

        # reverse nodes between left and right, example1: 4->3->2
        for _ in range(right-left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
        # after reversing between left and right, curr is node after right, prev is node at right

        left_prev.next.next = curr # have left node point to curr, example1: 2 -> 5
        left_prev.next = prev # have node before left point to prev, example1: -> 4

        return head_return.next