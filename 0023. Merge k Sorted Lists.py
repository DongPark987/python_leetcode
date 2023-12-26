import copy
from typing import List
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(0)
        heapq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heapq, (lists[i].val, i, lists[i]))

        while heapq:
            node = heappop(heapq)
            idx = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heappush(heapq, (result.next.val, idx, result.next))

        return root.next


a = MyStack()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(a.MyQueue(temperatures))
