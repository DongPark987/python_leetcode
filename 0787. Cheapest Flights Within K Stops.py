import sys
from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # flights = 출발, 도착, 코스트
        # 그래프 생성, 시작 -> (목적지, 코스트)
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))

        # 코스트,이동 가능 횟수 ,목적지,
        hq = [(0, src, k)]
        while hq:
            cost, d, cnt = heappop(hq)
            if d == dst:
                return cost
            if cnt >= 0:
                for link, link_cost in graph[d]:
                    tmp = cost + link_cost
                    heappush(hq, (tmp, link, cnt - 1))
        return -1


a = Solution()

n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

print(a.findCheapestPrice(n, flights, src, dst, k))
