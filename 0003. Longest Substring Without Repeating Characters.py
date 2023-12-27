import copy
from typing import List
from collections import deque


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         ans = 0
#         queue = deque()
#         for c in s:
#             if c in queue:
#                 while c in queue:
#                     queue.popleft()
#             queue.append(c)
#             ans = max(ans,len(queue))
#         return ans

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         q = deque()
#         ans = 0
#         for char in s:
#             while q and char in q:
#                 q.popleft()
#             q.append(char)
#             ans = max(ans, len(q))
#         return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = ans = 0
        visited = {}
        for i, char in enumerate(s):
            if char in visited and visited[char] >= start:
                start = visited[char] + 1
            visited[char] = i
            ans = max(ans, i - start + 1)
        return ans


a = Solution()

s = "abcabcbb"

print(a.lengthOfLongestSubstring(s))
