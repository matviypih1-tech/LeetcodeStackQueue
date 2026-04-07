class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, x: int) -> None:
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self._size += 1

    def dequeue(self) -> int:
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return value

    def peek(self) -> int:
        return self.head.value if self.head else None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

class MyStack:
    def __init__(self):
        self.queue = MyQueue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        for _ in range(self.queue.size() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self) -> int:
        return self.queue.dequeue()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()
