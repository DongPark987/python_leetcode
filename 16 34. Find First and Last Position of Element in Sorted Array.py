import bisect
import copy
from typing import List
from collections import deque


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1

        if 0 <= left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]


a = Solution()

nums = [2, 2]
target = 3

print(a.searchRange(nums, target))
