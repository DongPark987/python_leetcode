from typing import List
from typing import Optional
import math
from itertools import combinations


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digit_len = len(digit)
        ans = "0"
        for i in range(0, len(number), digit_len):
            find = number[i:i + digit_len]
            if find == digit:
                tmp = number[0:i] + number[i + digit_len:]
                ans = max(ans, tmp)
        return ans


a = Solution()
number = "1231"
digit = "1"

print(a.removeDigit(number, digit))
