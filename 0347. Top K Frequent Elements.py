import copy
from typing import List
from collections import deque, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]


a = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(a.topKFrequent(nums, k))
