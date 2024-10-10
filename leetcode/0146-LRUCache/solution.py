class DLLNode:
    """ Doubly Linked List Node, where each node has a key, value, prev and next pointers """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes to avoid edge cases
        self.dll_left, self.dll_right = DLLNode(0,0), DLLNode(0,0)
        self.dll_left.next = self.dll_right
        self.dll_right.prev = self.dll_left
        
    
    def remove_node(self, node):
        # Remove the node from the linked list (by updating prev and next pointers)
        node_prev, node_next = node.prev, node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def insert_node(self, node):
        # Insert the node at the end of the linked list (before dummy tail)
        prev, nxt = self.dll_right.prev, self.dll_right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def print_ll(self):
        # for debugging
        node = self.dll_left
        while node:
            print(node.key, node.value)
            node = node.next
        print()

    def get(self, key: int) -> int:
        # Update the linked list to move the node to the end, if it exists
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # Update the linked list to move the node to the end, if it exists
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = DLLNode(key, value)
        self.insert_node(self.cache[key])

        if self.capacity<len(self.cache):
            lru = self.dll_left.next
            self.remove_node(lru)
            del self.cache[lru.key]
        # self.print_ll()

# Your LRUCache object will be instantiated and called as such:

print("Test case 1: Capacity: 3, Put 1,2,3,4 and get 1")
print("Expected: -1 from get 1")
print("Actual:")
obj = LRUCache(3)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)

print(obj.get(1))