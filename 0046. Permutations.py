import copy
from typing import List
from collections import deque
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


a = Solution()

nums = [1, 2, 3]

print(a.permute(nums))
