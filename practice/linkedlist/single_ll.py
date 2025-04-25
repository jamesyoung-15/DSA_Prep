class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insertAtHead(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtHead(data)
            return
        curr_node = self.head
        i = 0
        while curr_node and i < index-1:
            curr_node = curr_node.next
            i+=1
        new_node = ListNode(data)
        if curr_node is None:
            curr_node.next = new_node
        else:
            new_node.next = curr_node.next
            curr_node.next = new_node

    def printLinkedList(self):
        curr = self.head
        while curr:
            print(f'{curr.data} ')
            curr = curr.next
    
    def deleteAtIndex(self, index):
        if index == 0:
            self.deleteAtHead()
            return
        curr_node = self.head
        i = 0
        while curr_node and i < index-1:
            curr_node = curr_node.next
            i+=1
        if curr_node.next:
            curr_node.next = curr_node.next.next

    def deleteAtHead(self):
        if not self.head:
            return
        new_head = self.head.next
        self.head.next = None
        self.head = new_head

new_list = LinkedList()
new_list.insertAtHead(1)
new_list.insertAtIndex(2,1)
new_list.insertAtIndex(3,2)
new_list.insertAtHead(0)
new_list.insertAtIndex(4,3)
new_list.deleteAtIndex(0)
new_list.printLinkedList()