class Node_list:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        node = Node_list(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return data

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, data):
        node = Node_list(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        self.size += 1

    def appendleft(self, data):
        node = Node_list(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        self.size -= 1
        return data

    def popleft(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        return data

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        node = Node_list(data)
        if not self.is_empty():
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.data

# TESTING

# QUEUE
print("--- 1. QUEUE ---")
q = Queue()

q.enqueue("p1")
q.enqueue("p2")
q.enqueue("p3")

print(f"Queue size: {q.size}")
print(f"Got: {q.dequeue()}")  # p1
print(f"Got: {q.dequeue()}")  # p2
print(f"Got: {q.dequeue()}")  # p3
print(f"Empty now? {q.is_empty()}\n")

# STACK
print("--- 2. STACK ---")
s = Stack()

s.push("p1")
s.push("p2")
s.push("p3")

print(f"Top item is: {s.peek()}")
print(f"Popped: {s.pop()}")  # p3
print(f"Popped: {s.pop()}")  # p2
print(f"Popped: {s.pop()}")  # p1
print(f"Empty now? {s.is_empty()}\n")

# DEQUE
print("--- 3. DEQUE ---")
d = Deque()

d.append("p2")  # standard push right
d.append("p3")  # adding to the tail
d.appendleft("p1")  # adding to the head

print(f"Deque size: {d.size}")

print(f"Pop from left: {d.popleft()}")  # p1
print(f"Pop from right: {d.pop()}")  # p3
print(f"Pop last one: {d.pop()}")  # p2
print(f"Empty now? {d.is_empty()}")

