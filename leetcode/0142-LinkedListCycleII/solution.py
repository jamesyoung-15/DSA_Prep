from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # creat dictionary to record nodes, if node exist in dictionary then it means that we have returned to beginning of cycle and can return it
        hash_map = {}
        result = None
        curr = head
        while curr:
            if curr in hash_map:
                return curr
            else:
                hash_map[curr] = 1
            curr = curr.next
        return result

# time: O(n), space: O(n)