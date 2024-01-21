from typing import List
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        ans = 0
        while q:
            ans += 1
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
        return ans


s = Solution()

data = [6, 2, 6, 5, 1, 2]
print(s.arrayPairSum(data))
