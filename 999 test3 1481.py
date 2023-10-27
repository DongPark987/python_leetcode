from typing import List
from typing import Optional
import math


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_cnt = {}
        for i in arr:
            if i in num_cnt:
                num_cnt[i] = num_cnt[i] + 1
            else:
                num_cnt[i] = 1
        num_cnt = sorted(num_cnt.items(), key=lambda x: x[1])
        remove_cnt = 0
        for key, value in num_cnt:
            if k >= value:
                k = k - value
                remove_cnt = remove_cnt + 1
            else:
                break

        return len(num_cnt) - remove_cnt


a = Solution()
arr = [1, 10, 3, 10, 2]
k = 1
print(a.findLeastNumOfUniqueInts(arr,k))
