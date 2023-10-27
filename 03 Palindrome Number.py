from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_list = list(str(x))
        reverse_list = list(reversed(num_list))
        if num_list == reverse_list:
            return True
        else:
            return False


a = Solution()

x = 121
print(a.isPalindrome(x))
