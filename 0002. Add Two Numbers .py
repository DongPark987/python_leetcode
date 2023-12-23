from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         node, prev = l1, None
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
#
#         num1 = 0
#         while prev:
#             num1 = num1 * 10 + prev.val
#             prev = prev.next
#         node, prev = l2, None
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
#         num2 = 0
#         while prev:
#             num2 = num2 * 10 + prev.val
#             prev = prev.next
#         ans = list(map(int, str(num1 + num2)))
#         ans.reverse()
#         head = ListNode(ans[0])
#         curr = head
#         for i in range(1, len(ans)):
#             curr.next = ListNode(ans[i])
#             curr = curr.next
#         return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next


a = Solution()

nums = [3, 3]
target = 6
print(a.twoSum(nums, target))
