from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of linked list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1
        # if we're deleting the head, then we need to update head node
        if length == n:
            head = head.next
            return head

        # iterate until right before the nth node
        i = length
        curr2 = head
        while curr2:
            # point node right before nth node to the one after nth node
            if i == n+1:
                if not curr2.next.next:
                    curr2.next = None
                else:
                    curr2.next = curr2.next.next
            i -= 1
            curr2 = curr2.next
        
        return head

# time: O(n), space: O(1)

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n = 1
test = Solution().removeNthFromEnd(n1,1)
print("List: [1,2,3], n = 1")
print("Output:")
while test:
    print(test.val)
    test = test.next
