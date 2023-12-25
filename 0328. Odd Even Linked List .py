from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         even_root = even = ListNode(0)
#         root = head
#         prev = None
#         while head and head.next:
#             even.next = head.next
#             next = head.next.next
#             head.next.next = None
#             head.next = next
#             even = even.next
#             prev = head
#             head = head.next
#         if not head:
#             if prev:
#                 prev.next = even_root.next
#         else:
#             head.next = even_root.next
#         return root

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head

a = Solution()

s = "(]"

print(a.oddEvenList(s))
