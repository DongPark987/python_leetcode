from typing import List
from typing import Optional
import math


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        ans = -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            tmp_m = m
            b_cnt = 0
            for flower in bloomDay:
                if flower <= mid:
                    b_cnt = b_cnt + 1
                    if b_cnt == k:
                        tmp_m = tmp_m - 1
                        b_cnt = 0
                else:
                    b_cnt = 0
            if tmp_m <= 0:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


a = Solution()
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(a.minDays(bloomDay, m, k))
