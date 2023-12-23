import copy
from typing import List


class Solution:
    ans = []
    def backtrack(self, myStr, left, n: int, end: int):
        if n == end-1:
            for i in range(left):
                myStr = myStr + ')'
            self.ans.append(myStr)
            return
        self.backtrack(myStr+"(", left + 1, n + 1, end)
        for i in range(left):
            tmp_str = myStr
            for j in range(i):
                tmp_str = tmp_str + ')'
            self.backtrack(tmp_str+")" + "(", left-i, n + 1, end)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack('(', 1, 0, n)
        # print(self.ans)
        return self.ans

        # return list(sorted(ans))


a = Solution()

n = 4

print(a.generateParenthesis(n))
