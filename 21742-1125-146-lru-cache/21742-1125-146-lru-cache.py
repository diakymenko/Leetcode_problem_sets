class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head


    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        node.prev = None
        node.next = None

    def delete_head(self):
        if not self.head:
            return None
        removed = self.head
        # remove head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.llist = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.llist.remove_node(node)
            self.llist.add_to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.llist.remove_node(node)
            self.llist.add_to_tail(node)
        else:
            # If over capacity, evict least recently used (head)
            if len(self.cache) >= self.capacity:
                removed_node = self.llist.delete_head()
                if removed_node:
                    del self.cache[removed_node.key]
            # Add new node
            new_node = Node(key, value)
            self.llist.add_to_tail(new_node)
            self.cache[key] = new_node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)