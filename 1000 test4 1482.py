from typing import List
from typing import Optional
import math
from itertools import combinations


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        left = 1
        right = len(nums) + 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            # print(mid)
            isTrue = False
            Max = 0
            Min = 9999999999
            for i in combinations(nums, mid):
                tmp_sum = sum(i)
                Max = max(Max, tmp_sum)
                Min = min(Min, tmp_sum)
                if tmp_sum == target:
                    isTrue = True
                    ans = max(ans, mid)
                    break
            print("max: ",Max)
            print("min: ",Min)
            if isTrue:
                left = mid + 1
                continue

            if Max < target:
                left = mid + 1
                continue

            if Min > target:
                right = mid - 1


            # if Max > target:
            #     right = mid - 1
            # else:
            #     left = mid + 1
        return ans


a = Solution()

nums = [4, 6, 15, 12, 15]
target = 37

print(a.lengthOfLongestSubsequence(nums, target))
