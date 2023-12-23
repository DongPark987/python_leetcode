import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


a = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(a.lengthOfLIS(nums))
