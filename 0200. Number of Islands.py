import copy
from typing import List
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


class Solution:
    visit = []

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(x, y):
            pass

        return grid
        pass


a = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(a.numIslands(grid))
