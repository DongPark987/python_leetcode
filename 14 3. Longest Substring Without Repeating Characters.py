import copy
from typing import List
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        queue = deque()
        for c in s:
            if c in queue:
                while c in queue:
                    queue.popleft()
            queue.append(c)
            ans = max(ans,len(queue))
        return ans


a = Solution()

s = "abcabcbb"

print(a.lengthOfLongestSubstring(s))
