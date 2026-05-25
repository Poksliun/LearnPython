class Node:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def is_empty(self):
        if not self.first:
            return 1
        return 0
    def look_first(self):
        if self.first:
            print(self.first.value)
    def append(self, value):
        if not self.last:
            self.last = Node(value)
            self.first = self.last
            return
        self.last.next = Node(value)
        self.last=self.last.next
    def pop(self):
        if self.first:
            if self.first.next:
                self.first=self.first.next

    def printAll(self):
        current = self.first
        while current:
            print(current.value)
            current = current.next

q = Queue()
q.append(3)
q.append(1000)
q.look_first()
q.pop()
q.printAll()