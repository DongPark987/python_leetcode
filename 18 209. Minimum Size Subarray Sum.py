import bisect
import copy
from typing import List
from collections import deque
import time


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums.sort()
        window = deque()
        curr_sum = 0
        ans = 9999999999
        for i in nums:
            window.append(i)
            curr_sum = curr_sum + i
            while curr_sum >= target:
                ans = min(ans, len(window))
                curr_sum = curr_sum - window.popleft()

        if ans == 9999999999:
            return 0
        return ans



a = Solution()

target = 15
nums = [1,2,3,4,5]

print(a.minSubArrayLen(target, nums))
