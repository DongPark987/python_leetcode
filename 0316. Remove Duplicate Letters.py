from typing import List
from collections import OrderedDict, defaultdict, Counter


# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             print(set(s), set(suffix))
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        s_counter = Counter(s)
        for char in s:
            s_counter[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and s_counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)


a = Solution()

s = "cbacdcbc"

print(a.removeDuplicateLetters(s))

# n1 = {1, 2, 3}
# n2 = {3, 2, 1}
# print(n1, n2)
