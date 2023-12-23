import collections
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        out = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            out[i] = out[i + 1] * nums[i + 1]
        for i in range(len(left)):
            out[i] *= left[i]
        return out


s = Solution()

nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
