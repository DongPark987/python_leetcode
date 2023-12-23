import copy
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        for i in intervals:
            if len(ans) == 0:
                ans.append(i)
            else:
                if ans[-1][1] >= i[0]:
                    if ans[-1][1] < i[1]:
                        ans[-1] = [ans[-1][0],i[1]]
                else:
                    ans.append(i)
        return ans


a = Solution()

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
target = 6

print(a.merge(intervals))
