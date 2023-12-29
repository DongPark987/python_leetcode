from typing import List
from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        my_dict = defaultdict(list)
        ans = []
        for f, t in sorted(tickets):
            my_dict[f].append(t)

        def dfs(curr):
            print(curr)
            while my_dict[curr]:
                dfs(my_dict[curr].pop(0))
            ans.append(curr)
        dfs('JFK')
        return ans[::-1]


s = Solution()

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(s.findItinerary(tickets))
