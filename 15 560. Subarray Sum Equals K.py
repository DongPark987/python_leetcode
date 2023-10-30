import copy
from typing import List
from collections import deque


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        prefix_sum = 0
        # 모드 서브 어레이의 합을 저장하는 딕셔너리
        # 현제의 prefix 총합에서 제거하여 k를 만들어 낼 수 있는 값을 찾을 수 있다
        d = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in d:
                result += d[prefix_sum - k]
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1
        return result


a = Solution()

nums = [1, 1, 1]
k = 2

print(a.subarraySum(nums, k))
