import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        dp[0] = -prices[0]
        ans = 0
        for i in range(1, len(prices)):
            ans = max(ans,dp[i-1]+prices[i])
            dp[i] = max(dp[i-1],-prices[i])
        return ans


a = Solution()

prices = [7,1,5,3,6,4]

print(a.maxProfit(prices ))
