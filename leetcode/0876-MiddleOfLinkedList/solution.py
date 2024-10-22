from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node1 = head
        # find total length
        while node1:
            length+=1
            node1 = node1.next
        
        # go to middle
        middle = (length-1)//2
        counter = 0
        node2 = head
        while node2 and counter<middle:
            counter += 1
            node2 = node2.next
        if length%2==0:
            node2 = node2.next
        return node2
    
