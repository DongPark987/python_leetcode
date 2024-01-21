import copy
from typing import List
from collections import defaultdict, Counter


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)

        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        leaves = []
        for i in graph:
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            next_leaves = []
            for i in leaves:
                value = graph[i].pop()
                graph[value].remove(i)
                if len(graph[value]) == 1:
                    next_leaves.append(value)
            leaves = next_leaves
        return leaves


a = Solution()

n = 6

data = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]

print(a.findMinHeightTrees(n, data))
