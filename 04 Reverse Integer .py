from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        num_str = list(str(abs(x)))
        num_str.reverse()
        if x<0:
            return -int(''.join(num_str))
        else:
            return int(''.join(num_str))



a = Solution()

x = 123
print(a.reverse(x))
