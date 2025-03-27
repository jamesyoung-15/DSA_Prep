class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def solution(head: ListNode):
    # problem: remove duplicates from unsorted Linked List
    # solution: use hashmap to keep track of duplicates
    # time complexity: O(n), space complexity: O(n)
    if head is None:
        return head
    seen = {head.val}
    node = head
    while node.next is not None:
        # check if next node is a duplicate
        if node.next.val in seen:
            node.next = node.next.next
        else:
            seen.add(node.next.val)
            node = node.next
    return head

def print_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

# 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print_list(head)
head = solution(head)
print_list(head)