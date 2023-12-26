import copy
from typing import List
from collections import deque


class MyStack:
    def __init__(self):
        self.my_deque = deque()

    def push(self, x: int) -> None:
        self.my_deque.append(x)
        for _ in range(len(self.my_deque) - 1):
            self.my_deque.append(self.my_deque.popleft())

    def pop(self) -> int:
        return self.my_deque.popleft()

    def top(self) -> int:
        return self.my_deque[0]

    def empty(self) -> bool:
        return 0 == len(self.my_deque)


a = MyStack()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(a.dailyTemperatures(temperatures))
