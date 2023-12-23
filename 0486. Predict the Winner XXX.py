import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        curr = 0
        score = [0, 0]

        while nums:
            if nums[0] >= nums[-1]:
                score[curr] += nums[0]
                nums.pop(0)
            else:
                score[curr] += nums[-1]
                nums.pop(-1)
            if curr == 0:
                curr = 1
            else:
                curr = 0
        if score[0] >= score[1]:
            return True
        else:
            return False


a = Solution()

nums = [1,5,233,7]

print(a.predictTheWinner(nums))
