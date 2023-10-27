from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        length = len(nums)
        ans = 0
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] != nums[j] != nums[k] != nums[i]:
                        ans = ans + 1
        return ans


a = Solution()

nums = [4, 4, 2, 4, 3]
print(a.unequalTriplets(nums))
