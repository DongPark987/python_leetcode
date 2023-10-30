from typing import List
from typing import Optional
from collections import Counter
import math


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_cnt = sorted(Counter(arr).items(), key=lambda x: x[1])
        remove_cnt = 0
        for key, value in num_cnt:
            if k >= value:
                k -= value
                remove_cnt += 1
            else:
                break
        return len(num_cnt) - remove_cnt


a = Solution()
arr = [1]
k = 1
print(a.findLeastNumOfUniqueInts(arr, k))
