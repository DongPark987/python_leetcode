import bisect
import copy
import sys
from typing import List
from collections import deque
from collections import defaultdict

import time


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1 or (list2 and list1.val > list2.val):
#             list1, list2 = list2, list1
#         if list1:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#         return list1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        while curr is not None and list2 is not None:
            if curr.next is not None and curr.next.val == list2.val:
                curr = curr.next
                tmp_list2 = curr.next
                curr.next = list2
                list2 = tmp_list2
            elif curr.next is not None and curr.next.val < list2.val:
                tmp_list2 = curr.next
                curr.next = list2
                list2 = tmp_list2
            else:
                curr = curr.next

        return list1



a = Solution()

prices = [7, 1, 5, 3, 6, 4]

print(a.mergeTwoLists(prices))
