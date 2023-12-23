import bisect
import copy
from typing import List
from collections import deque
import time


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def reverse(node: ListNode, prev: ListNode = None):
#             if node == None:
#                 return prev
#             else:
#                 next, node.next = node.next, prev
#                 return reverse(next, node)
#         return reverse(head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, Nonde
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev


a = Solution()

data = []
print(a.reverseList(data))
