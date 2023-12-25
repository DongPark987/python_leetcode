from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        root = start = ListNode(0)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next


s = Solution()

head = [1, 2, 3, 4, 5]
root = ListNode(0)
cur = root
for i in head:
    cur.next = ListNode(i)
    cur = cur.next
left = 2
right = 4

ans = s.reverseBetween(root.next, left, right)

while ans:
    print(ans.val)
    ans = ans.next
