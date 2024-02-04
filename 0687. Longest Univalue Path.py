# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        val = 0

        def dfs(root, parent):
            nonlocal val
            if root is None:
                return 0
            tmp1 = dfs(root.left, root)
            tmp2 = dfs(root.right, root)
            print(tmp1, tmp2)
            val = max(val, tmp1 + tmp2)

            if root.val == parent.val:
                return max(tmp1 + 1, tmp2 + 1)
            else:
                return 0

        dfs(root, root)
        return val


a = Solution()
