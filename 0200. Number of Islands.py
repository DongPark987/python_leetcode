import copy
from typing import List
from collections import deque




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w, h = len(grid[0]), len(grid)
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        visit = [[False for _ in range(w)] for _ in range(h)]
        ans = 0

        def dfs(x, y):
            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]
                if tx < 0 or tx >= w or ty < 0 or ty >= h or grid[ty][tx] == '0' or visit[ty][tx]:
                    continue
                visit[ty][tx] = True
                dfs(tx, ty)

        for i in range(h):
            for j in range(w):
                if not visit[i][j] and grid[i][j] == '1':
                    visit[i][j] = True
                    dfs(j, i)
                    ans += 1

        return ans


a = Solution()

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(a.numIslands(grid))
