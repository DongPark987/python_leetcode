import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    l = {}
    vd = {}
    visit = {}
    ans = 0.0

    def dfs(self, src, det, num):
        for i in self.l[src]:
            if i == det:
                self.ans = num * self.vd[src + "-" + i]
                return
            if i in self.l and src + i not in self.visit:
                self.visit[src + i] = True
                self.dfs(i, det, num * self.vd[src + "-" + i])

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.l = {}
        self.vd = {}
        e = equations
        v = values
        result = []
        for i in range(len(e)):
            if e[i][0] in self.l:
                self.l[e[i][0]].append(e[i][1])
            else:
                self.l[e[i][0]] = [e[i][1]]

            if e[i][1] in self.l:
                self.l[e[i][1]].append(e[i][0])
            else:
                self.l[e[i][1]] = [e[i][0]]

            self.vd[e[i][0] + "-" + e[i][1]] = v[i]
            self.vd[e[i][1] + "-" + e[i][0]] = 1 / v[i]

        for i in queries:
            self.visit = {}
            if i[0] not in self.l or i[1] not in self.l:
                result.append(-1.0)
                continue
            if i[0] == i[1]:
                result.append(1.0)
                continue

            self.ans = -1.0
            if i[0] in self.l:
                self.dfs(i[0], i[1], 1)
            result.append(self.ans)
        return result


a = Solution()

equations = [["a", "b"], ["ab", "c"], ["a", "bc"]]
values = [2.0, 3.0, 4.0]
queries = [["a", "c"], ["b", "a"], ["ab", "c"], ["a", "a"], ["x", "x"]]

print(a.calcEquation(equations, values, queries))
