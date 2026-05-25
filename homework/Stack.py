class Node:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self):
        self.head = None

    def look_first(self):
        if self.head:
            print(self.head.value)

    def append_on_start(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.head:
            if self.head.next:
                value = self.head.value
                self.head=self.head.next
                return value
            else:
                value = self.head.value
                self.head = None
                return value

    def printAll(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

q = Stack()
q.append_on_start(1)
q.append_on_start(1000)
q.pop()
q.printAll()