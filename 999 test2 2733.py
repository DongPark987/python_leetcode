from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        nums.sort()
        return nums[1]



a = Solution()
nums = [3,2,1,4]
nums = [1,2]
print(a.findNonMinOrMax(nums))
