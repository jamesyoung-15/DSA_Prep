from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and curr.val>stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        print(stack)
        new_head = ListNode(0)
        new_curr = new_head
        for num in stack:
            new_curr.next = ListNode(num)
            new_curr = new_curr.next


        return new_head.next

ll_list = [5,2,13,12,8]
ll = ListNode(5)
curr = ll
for i in range(1,len(ll_list)):
    curr.next = ListNode(ll_list[i])
    curr = curr.next

test = Solution().removeNodes(ll)
curr = test
while curr:
    print(curr.val)
    curr = curr.next