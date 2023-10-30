import math
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        max2 = -math.inf
        for i in reversed(range(len(nums))):
            if nums[i] < max2:
                return True
            while stack and stack[-1] < nums[i]:
                max2 = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False


a = Solution()

nums = [3, 5, 0, 3, 4]

print(a.find132pattern(nums))
