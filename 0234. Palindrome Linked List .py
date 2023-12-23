import copy
from typing import List
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q = deque()
#         while head is not None:
#             q.append(head.val)
#             head = head.next
#         while len(q)>=2:
#             if q.pop() != q.popleft():
#                 return False
#         return True

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        reverse_list = []
        while slow is not None:
            if fast is not None:
                fast = fast.next
                if fast is not None:
                    reverse_list.append(slow.val)
                    fast = fast.next
            else:
                if reverse_list.pop() != slow.val:
                    return False
            slow = slow.next
        return True


a = Solution()


print(a.addOperators(num, target))
