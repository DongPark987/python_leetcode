from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i in range(len(nums)):
            a[nums[i]] = i

        print(a)
        for i in range(len(nums)):
            if target - nums[i] in a and i != a[target - nums[i]]:
                return [i, a[target - nums[i]]]


a = Solution()

nums = [3,3]
target = 6
print(a.twoSum(nums, target))
