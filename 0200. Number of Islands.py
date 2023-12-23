import bisect
import copy
from typing import List
from collections import deque
import time


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        M = len(grid[0])
        N = (len(grid))
        ans = 0
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(N):
            for j in range(M):
                if not visit[i][j] and grid[i][j] == '1':
                    q = deque()
                    q.append([j, i])
                    visit[i][j] = True
                    while len(q) != 0:
                        x, y = q.popleft()
                        for k in range(4):
                            tx = x + dx[k]
                            ty = y + dy[k]
                            if 0 <= tx < M and 0 <= ty < N and visit[ty][tx] == False and grid[ty][tx] == '1':
                                visit[ty][tx] = True
                                q.append([tx, ty])
                    ans = ans + 1
        return ans


a = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(a.numIslands(grid))
