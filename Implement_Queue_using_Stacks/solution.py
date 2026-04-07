class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1

    def pop(self) -> int:
        if self.is_empty():
            return None
        value = self.top_node.value
        self.top_node = self.top_node.next
        self._size -= 1
        return value

    def peek(self) -> int:
        if self.is_empty():
            return None
        return self.top_node.value

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.top_node is None

class MyQueue:
    def __init__(self):
        self.stack_in = MyStack()
        self.stack_out = MyStack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def _move(self) -> None:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move()
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()
class MyQueue:
    def __init__(self):
        self.stack_in = MyStack()
        self.stack_out = MyStack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def _move(self) -> None:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move()
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()
