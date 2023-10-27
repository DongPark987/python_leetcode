from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        curr = root
        ans = []
        for target in queries:
            tmp_ans = [-1, -1]
            # small or equal
            curr = root
            while curr is not None:
                if curr.val <= target:
                    if tmp_ans[0] == -1 or abs(curr.val - target) < abs(tmp_ans[0] - target):
                        tmp_ans[0] = curr.val

                if curr.val < target:
                    curr = curr.right
                elif curr.val > target:
                    curr = curr.left
                elif curr.val == target:
                    break

            curr = root
            # bigger or equal
            while curr is not None:
                if curr.val >= target:
                    if tmp_ans[1] == -1 or abs(curr.val - target) < abs(tmp_ans[1] - target):
                        tmp_ans[1] = curr.val

                if curr.val < target:
                    curr = curr.right
                elif curr.val > target:
                    curr = curr.left
                elif curr.val == target:
                    break
            ans.append(tmp_ans)

        return ans


a = Solution()
nums = [4, 4, 2, 4, 3]
print(a.unequalTriplets(nums))
