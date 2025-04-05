from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution: create dummy node and store two adjacent nodes, perform swap by moving pointers then move past swapped nodes
        # time: O(n), space: O(1)
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            # swap adjacent nodes
            first = curr.next
            second = curr.next.next
            first.next = second.next
            second.next = first
            # move past swapped nodes
            curr.next = second
            curr = curr.next.next
        return dummy.next

# Test cases
def create_linked_list(arr):
    head = ListNode(arr[0])
    curr = head
    for i in arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Test case 1
head = create_linked_list([1, 2, 3, 4])
solution = Solution()
result = solution.swapPairs(head)
print_linked_list(result)  # Expected output: 2 -> 1 -> 4 -> 3 -> None