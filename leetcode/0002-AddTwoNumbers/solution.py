from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse the nodes, multiply each node value by 10^n, where n starts from 0
        n1 = 0
        l1_val = 0
        l1_curr = l1
        while l1_curr is not None:
            l1_val += l1_curr.val * 10 ** n1
            n1 += 1
            l1_curr = l1_curr.next
        # repeat for l2
        n2 = 0
        l2_val = 0
        l2_curr = l2
        while l2_curr is not None:
            l2_val += l2_curr.val * 10 ** n2
            n2 += 1
            l2_curr = l2_curr.next
        
        total = str(l1_val + l2_val)
        answer_head = ListNode()
        answer_curr = answer_head
        for i in range(len(total)-1,-1,-1):
            answer_node = ListNode(int(total[i]))
            answer_curr.next = answer_node
            answer_curr = answer_curr.next

        return answer_head.next

l1_head = ListNode(2)
l1_node_1 = ListNode(4)
l1_node_2 = ListNode(3)
l1_head.next = l1_node_1
l1_node_1.next = l1_node_2 
l2_head = ListNode(5)
l2_node_1 = ListNode(6)
l2_node_2 = ListNode(4)
l2_head.next = l2_node_1
l2_node_1.next = l2_node_2 


l1 = l1_head
l2 = l2_head
test = Solution().addTwoNumbers(l1,l2)

while test is not None:
    print(test.val)
    test = test.next