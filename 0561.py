from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(list(sorted(nums))[::2])

s = Solution()

data = [6, 2, 6, 5, 1, 2]
print(s.arrayPairSum(data))
