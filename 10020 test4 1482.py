from typing import List
from typing import Optional
from collections import deque
import math
from itertools import combinations


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = 0
        window = deque()
        ans = 0
        for i in nums:
            if sum < target:
                sum+=i
                window.append(i)
            else:
                sum-= window.popleft()
                sum+=i
                window.append(i)



a = Solution()

nums = [3,11,5,3,10,4]
target = 18

print(a.lengthOfLongestSubsequence(nums, target))
