import copy
from typing import List
from collections import defaultdict, Counter


# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         dict = defaultdict(int)
#         for char in stones:
#             dict[char] += 1
#         ans = 0
#         for char in jewels:
#             ans += dict[char]
#         return ans

# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         dict = Counter(stones)
#         ans = 0
#         for char in jewels:
#             ans += dict[char]
#         return ans

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)


a = Solution()

jewels = "aA"
stones = "aAAbbbb"

print(a.numJewelsInStones(jewels, stones))
