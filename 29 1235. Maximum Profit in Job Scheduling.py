import bisect
import copy
from typing import List
from collections import deque
from collections import defaultdict

import time


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans


a = Solution()

height = [1, 2, 4, 3]

print(a.maxArea(height))
