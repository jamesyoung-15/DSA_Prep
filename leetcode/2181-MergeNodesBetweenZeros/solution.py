from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # go through linked list starting at second node, if we reach a 0 create new node of tracked sum and add to result linked list, otherwise update tracked sum
        # time: O(n), space: O(n)
        
        sum_tracker = 0
        result_node = ListNode()
        return_node = result_node
        curr = head.next
        while curr:
            if curr.val == 0:
                new_node = ListNode(sum_tracker)
                result_node.next = new_node
                result_node = result_node.next
                sum_tracker = 0
            else:
                sum_tracker += curr.val

            curr = curr.next


        return return_node.next