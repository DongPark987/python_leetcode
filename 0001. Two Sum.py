from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         a = dict()
#         for i in range(len(nums)):
#             a[nums[i]] = i
# 
#         print(a)
#         for i in range(len(nums)):
#             if target - nums[i] in a and i != a[target - nums[i]]:
#                 return [i, a[target - nums[i]]]
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums):
#             comp = target - n
#             if comp in nums[i + 1:]:
#                 return [i, nums[i + 1:].index(comp) + i + 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, value in enumerate(nums):
            if target - value in my_map:
                return [i, my_map[target - value]]
            my_map[value] = i
            


a = Solution()

nums = [3,3]
target = 6
print(a.twoSum(nums, target))
