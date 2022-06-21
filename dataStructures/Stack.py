## Array implementation
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

## Linked list implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        
        return self.head.next.value
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")

        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

