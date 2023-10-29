from typing import List
from typing import Optional


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        return sorted(nums[:3])[1]


a = Solution()
nums = [3, 2, 1, 4]
# nums = [1, 2]
print(a.findNonMinOrMax(nums))
