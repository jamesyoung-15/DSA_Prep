class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def insertAtHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    
    def insertAtIndex(self, val, index):
        if index == 0:
            self.insertAtHead(val)
            return
        curr = self.head
        i = 0
        while curr and i<index-1:
            curr = curr.next
            i+=1
        
        if curr is None:
            return
        
        new_node = ListNode(val)
        new_node.prev = curr
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
    
    def deleteAtHead(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        new_head = self.head.next
        new_head.prev = None
        self.head.next = None
        self.head = new_head
    
    def deleteAtIndex(self, index):
        if index == 0:
            self.deleteAtHead()
            return
        curr = self.head
        i = 0
        while curr and i<index:
            curr = curr.next
            i+=1
        if curr is None:
            return
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next
        


    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
    def printBackwards(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.val)
            curr = curr.prev


new_list = LinkedList(ListNode(1))
new_list.insertAtHead(0)
new_list.insertAtIndex(2,2)
new_list.insertAtIndex(3,3)
new_list.printLinkedList()
new_list.deleteAtHead()
print()
new_list.printLinkedList()
new_list.deleteAtIndex(2)
print()
new_list.printLinkedList()