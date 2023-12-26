import copy
from typing import List


class MyQueue:

    def __init__(self):
        self.stack = []
        self.out = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.out:
            while self.stack:
                self.out.append(self.stack.pop())
        return self.out.pop()

    def peek(self) -> int:
        if not self.out:
            while self.stack:
                out.append(self.stack.pop())
        return self.out[-1]

    def empty(self) -> bool:
        return (len(self.stack) + len(self.out)) == 0


a = MyStack()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(a.MyQueue(temperatures))
