import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = True
                ans = s[i - 1:i + 1]

        for window in range(2, n + 1):
            for i in range(0, n - window):
                if s[i] == s[i + window] and dp[i + 1][i + window - 1] == True:
                    dp[i][i + window] = True
                    ans = s[i:i + window + 1]

        # for i in range(n):
        #         #     tmp = list(map(int, dp[i]))
        #         #     print(tmp)
        return ans


a = Solution()

s = "babad"

print(a.longestPalindrome(s))
