import bisect
import copy
import sys
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     dp = [0 for _ in range(len(prices))]
    #     dp[0] = prices[0]
    #     ans = 0
    #     for i in range(1, len(prices)):
    #         ans = max(ans, prices[i] - dp[i - 1])
    #         dp[i] = min(dp[i - 1], prices[i])
    #     return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min = sys.maxsize
        max_price = 0
        for i in prices:
            max_price = max(max_price, i - Min)
            Min = min(Min, i)
        return max_price


a = Solution()

prices = [7, 1, 5, 3, 6, 4]

print(a.maxProfit(prices))
