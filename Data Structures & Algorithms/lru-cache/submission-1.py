class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = None
        
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key][0]
            node = self.cache[key][1]
            self.dll.remove_node(node)
            self.dll.add_to_tail(node)
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dll.remove_node(self.cache[key][1])
        new_node = Node(key, value)
        self.cache[key] = (value, new_node)

        if not self.dll:
            self.dll = DoublyLinkedList(new_node, new_node)
        else:
            if len(self.cache) > self.capacity:
                del self.cache[self.dll.head.key]
                self.dll.remove_node(self.dll.head)
            self.dll.add_to_tail(new_node)
        

class DoublyLinkedList:

    def __init__(self, head: 'Node', tail: 'Node'):
        self.head = head
        self.tail = tail
    
    def remove_node(self, node):
        if node == self.head:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
                return
            self.head.prev = None
        elif node == self.tail:
            prev_node = node.prev
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

    def add_to_tail(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
        else:
            self.head = node
            self.head.prev = None
            self.head.next = None
            self.tail = node
            self.tail.next = None
            self.tail.prev = None
        

class Node:

    def __init__(self, key: int = -1, value: int = 0, prev: 'Node' = None, next: 'Node' = None):
        self.key = int(key)
        self.value = int(value)
        self.prev = prev
        self.next = next
