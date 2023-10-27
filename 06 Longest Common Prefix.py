from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Min_length = 999
        for i in strs:
            Min_length = min(Min_length, len(i))
        for i in range(Min_length):
            c = strs[0][i]
            for j in strs:
                if c != j[i]:
                    return strs[0][0:i]
        return strs[0][0:Min_length]


a = Solution()

# strs = ["flower", "flow", "flight"]
strs = [""]

print(a.longestCommonPrefix(strs))
