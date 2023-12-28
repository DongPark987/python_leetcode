import copy
from typing import List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        number = list(digits)
        ans = []
        end = len(digits)
        if end == 0:
            return []

        def dfs(loc, sum):
            if loc == end:
                ans.append(sum)
                return
            for char in dict[number[loc]]:
                dfs(loc + 1, sum + char)

        dfs(0, '')
        return ans


a = Solution()

digits = "23"

print(a.letterCombinations(digits))
