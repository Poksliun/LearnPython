class Node:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head= None

    def append_on_start(self,value):
        self.head = Node(value, self.head)

    def append_on_end(self, value):
        if not self.head:
            self.head = Node(value, self.head)
            return
        current = self.head
        while current.next:
            current=current.next
        current.next = Node(value)

    def printAll(self):
        current = self.head
        while current:
            print(current.value)
            current= current.next






q = SinglyLinkedList()
q.append_on_start(1)
q.append_on_start(1000)
q.append_on_end(3)
q.printAll()