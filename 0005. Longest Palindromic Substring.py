import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ''
#         n = len(s)
#         dp = [[False for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
#             ans = s[i]
#         for i in range(1, n):
#             if s[i] == s[i - 1]:
#                 dp[i - 1][i] = True
#                 ans = s[i - 1:i + 1]
# 
#         for window in range(2, n + 1):
#             for i in range(0, n - window):
#                 if s[i] == s[i + window] and dp[i + 1][i + window - 1] == True:
#                     dp[i][i + window] = True
#                     ans = s[i:i + window + 1]
# 
#         # for i in range(n):
#         #         #     tmp = list(map(int, dp[i]))
#         #         #     print(tmp)
#         return ans
    
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         ans = s[0]
#
#         for i in range(len(s)):
#             dp[i][i] = True
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 ans = s[i:i + 2]
#
#         for i in range(2, len(s)):
#             for j in range(len(s) - i):
#                 if s[j] == s[j + i] and dp[j + 1][j + i - 1]:
#                     dp[j][j + i] = True
#                     ans = s[j:j + i + 1]
#
#         return ans

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        if len(s) < 2 or s == s[::-1]:
            return s
        for i in range(len(s) - 1):
            ans = max(ans, expand(i, i + 1), expand(i, i + 2), key=len)
        return ans


a = Solution()

s = "babad"

print(a.longestPalindrome(s))
