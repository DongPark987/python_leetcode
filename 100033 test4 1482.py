from typing import List
from typing import Optional
import math
from itertools import combinations

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        longest = [0 for i in range(target+1)]
        for e in nums:
            for i in reversed(range(target+1-e)):
                if i == 0 or longest[i] != 0:
                    longest[e+i] = max(longest[e+i], longest[i] + 1)
        return longest[target] if longest[target] != 0 else -1

a = Solution()

nums = [4, 6, 15, 12, 15]
target = 37

print(a.lengthOfLongestSubsequence(nums, target))
