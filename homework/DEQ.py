class DEQ:
    def __init__(self):
        self.first = None
        self.last = None
        self.size =0

    def append_last(self, value):
        if not self.last:
            self.last = Node(value, None,None)
            self.first = self.last
            self.size+=1
            return
        self.last.next = Node(value,self.last,None)
        self.last = self.last.next
        self.size += 1
    def append_first(self, value):
        if self.first:
            current = Node(value,None,self.first)
            self.first.prev = current
            self.first = current
            self.size += 1
            return
        else:
            self.last = Node(value, None, None)
            self.first = self.last
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
        return self.first is None
    def delete_last(self):
        if self.size == 1:
            value = self.first.value
            self.first = None
            self.last = None
            self.size = 0
            return value
        elif self.first:
            value = self.last.value

            self.last = self.last.prev
            self.last.next = None
            self.size-=1
            return value
        else:
            print('ваш deq пуст')

    def delete_first(self):
        if self.size == 1:
            value = self.first.value
            self.first = None
            self.last = None
            self.size = 0
            return value
        elif self.first:
            value = self.first.value
            self.first = self.first.next
            self.first.prev=None
            self.size -= 1
            return value
        else:
            print('ваш deq пуст')