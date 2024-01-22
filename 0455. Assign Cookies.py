import sys
from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort(key=lambda x: -x)
        ans = 0

        for i in g:
            while s:
                if i <= s[-1]:
                    ans += 1
                    s.pop()
                    break
                s.pop()
                if len(s) == 0:
                    return ans

        return ans


a = Solution()

g = [1, 2, 3]
s = [1, 2]

print(a.findContentChildren(g, s))
