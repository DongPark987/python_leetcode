from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans[0] = max(ans[0], abs(left + right))
            print(left, right)
            return max(left + 1, right + 1)

        dfs(root)
        return ans[0]


s = Solution()

data = [6, 2, 6, 5, 1, 2]
print(s.arrayPairSum(data))
