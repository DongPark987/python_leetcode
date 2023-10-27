import copy
from typing import List


class Solution:
    piece = []
    ans = 0
    n = 0

    def check(self, x, y):
        for i in range(y):
            px = self.piece[i][0]
            py = self.piece[i][1]
            if x == px or abs(x - px) == abs(y - py):
                return False
        return True

    def rec(self, loc):
        if self.n == loc:
            self.ans = self.ans + 1
            return
        for i in range(self.n):
            if self.check(i, loc):
                self.piece[loc] = [i, loc]
                self.rec(loc + 1)

    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.piece = [[0 for _ in range(2)] for _ in range(n)]
        self.rec(0)
        return self.ans


a = Solution()

n = 1

print(a.totalNQueens(n))
