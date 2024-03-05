
# singly linked list
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
    

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or self.head is None:
            return -1
        node = self.head
        for i in range(index):
            node = node.next
        return node.val
    
    

    def addAtHead(self, val: int) -> None:
        node = Node(val)
       
        node.next = self.head
        self.head = node
        self.size += 1
        

            

    def addAtTail(self, val: int) -> None:
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1
        

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        
        node = self.head
        for i in range(index-1):
            node = node.next
        curr = node
        if curr.next:
            next_node = curr.next
            new_node = Node(val)
            curr.next = new_node
            new_node.next = next_node

        self.size += 1
     

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1


# class Node:
#     def __init__(self, val):
#         self.next = None
#         self.val = val
#         self.prev = None

# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
    
#     def get(self, index):
#         if index < 0 or index >= self.size or self.head is None:
#             return -1
#         node = self.head
#         for i in range(index):
#             node = node.next
#         return node.val

    
        