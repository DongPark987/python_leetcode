import sys
from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val+=root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root


a = Solution()

n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

print(a.findCheapestPrice(n, flights, src, dst, k))
