from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first find length of linked list
        length = 0
        len_node = head
        while len_node:
            len_node = len_node.next
            length+=1
        
        # find middle, then traverse to it
        middle = (length-1)//2
        i = 0
        mid_node = head
        while mid_node and i<=middle:
            mid_node = mid_node.next
            i+=1
        
        # reverse 2nd half of linked list
        prev = None
        curr = mid_node
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        # compare reversed 2nd half vs 1st half of list
        node = head
        while prev and node:
            if prev.val != node.val:
                return False
            node = node.next
            prev = prev.next
        return True