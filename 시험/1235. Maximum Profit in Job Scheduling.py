import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:


a = Solution()

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(a.jobScheduling(startTime,endTime,profit))
