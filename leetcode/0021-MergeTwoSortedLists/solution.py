from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ''' merge sort approach '''
        l1 = list1
        l2 = list2
        result = ListNode(-1)
        result_curr = result
        # compare and add l1 and l2 nodes until one or both of them reaches end
        while l1 and l2:
            if l1.val<=l2.val:
                result_curr.next = ListNode(l1.val)
                result_curr = result_curr.next
                l1 = l1.next
            else:
                result_curr.next = ListNode(l2.val)
                result_curr = result_curr.next
                l2 = l2.next
        # add remainders if any
        while l1:
            result_curr.next = ListNode(l1.val)
            result_curr = result_curr.next
            l1 = l1.next
        while l2:
            result_curr.next = ListNode(l2.val)
            result_curr = result_curr.next
            l2 = l2.next
        return result.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

test = Solution().mergeTwoLists(l1,l2)
while test:
    print(test.val)
    test = test.next