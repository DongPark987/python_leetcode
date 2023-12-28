import copy
from typing import List
from collections import deque
from itertools import combinations


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []
#
#         def dfs(loc, start, sum):
#             if loc == k:
#                 ans.append(sum[:])
#                 return
#             else:
#                 for i in range(start, n + 1):
#                     sum.append(i)
#                     dfs(loc + 1, i + 1, sum)
#                     sum.pop()
#         dfs(0, 1, [])
#         return ans
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))


a = Solution()

n = 4
k = 2

print(a.combine(n, k))
