class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index):
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index + 1):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        prev = self.getPrev(index)
        return prev.next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        prev = self.getPrev(index)
        new_node = ListNode(val)
        next_node = prev.next
        prev.next = new_node
        new_node.prev = prev
        new_node.next = next_node
        next_node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.getPrev(index)
        prev.next = prev.next.next
        prev.next.prev = prev
        self.size-=1
    
    def printLL(self):
        curr = self.head
        ll = ""
        for _ in range(self.size+1):
            ll += str(curr.val) + " "
            curr = curr.next
        print(ll)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)