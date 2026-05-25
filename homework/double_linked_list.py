class Node:
    def __init__(self, value, prev,next):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size =0

    def append(self, value):
        if not self.last:
            self.last = Node(value, None, None)
            self.first = self.last
            self.size+=1
            return
        self.last.next = Node(value,self.last, None)
        self.last = self.last.next
        self.size += 1
    def printAll(self):
        current = self.first
        while current:
            print(current.value)
            current = current.next
    def printAllBackward(self):
        current = self.last
        while current:
            print(current.value)
            current = current.prev
    def is_empty(self):
        if not self.first:
            return 1
        return 0
    def pop(self, number):
        if self.size>number:
            current = self.first
            for i in range(number):
                current=current.next
            if current.next and current.prev:
                next = current.next
                current=current.prev
                current.next= next
            elif current.next and not current.prev:
                self.first = current.next
            elif not current.next and current.prev:
                current.prev.next=None
            else:
                self.first = None
                self.last = None
        else:
            print("нет индекса с таким элементом")



d = DoublyLinkedList()
d.append(1)
d.append(1)
d.pop(0)
d.printAll()
