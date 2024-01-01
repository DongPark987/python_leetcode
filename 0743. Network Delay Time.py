from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop
import math


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [6000000 for _ in range(n + 1)]
        distance[0] = 0
        graph = defaultdict(list)
        for e in times:
            graph[e[0]].append((e[1], e[2]))
        hq = [(0, k)]

        while hq:
            cost, dst = heappop(hq)
            if distance[dst] > cost:
                distance[dst] = cost
                for dst, edge_cost in graph[dst]:
                    heappush(hq, (cost + edge_cost, dst))
        Max = max(distance)
        if Max == 6000000:
            return -1
        else:
            return Max




a = Solution()

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

print(a.networkDelayTime(times, n, k))
