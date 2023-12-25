from typing import List


# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         while curr and curr.next:
#             curr.val, curr.next.val = curr.next.val, curr.val
#             curr = curr.next.next
#         return head

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


a = Solution()

s = "(]"

print(a.swapPairs(s))
