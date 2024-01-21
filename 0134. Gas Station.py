import copy
from typing import List
from collections import defaultdict, Counter


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0,0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

a = Solution()

gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
# print(cost)
print(a.canCompleteCircuit(gas, cost))
