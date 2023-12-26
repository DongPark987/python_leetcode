import copy
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans


a = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(a.dailyTemperatures(temperatures))
