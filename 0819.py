from typing import List
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        count = collections.Counter(words)
        return count.most_common(1)[0][0]


s = Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(s.mostCommonWord(paragraph, banned))
