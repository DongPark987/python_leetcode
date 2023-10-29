import bisect
import copy
import heapq
from typing import List
from heapq import heappush
from collections import deque
import time
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         left = 0
#         right = len(nums) - 1
#
#         while True:
#             mid = random.randint(left, right)
#             # mid = (left + right) // 2
#             pivot = nums[mid]
#             # print(f"L: {left}, R: {right}, 피벗: {pivot}")
#             nums[mid], nums[right] = nums[right], nums[mid]
#             # print(nums)
#
#             stored_index = left
#             for i in range(left, right):
#                 if nums[i] < pivot:
#                     nums[i], nums[stored_index] = nums[stored_index], nums[i]
#                     stored_index += 1
#             nums[right], nums[stored_index] = nums[stored_index], nums[right]
#
#             # print("분배끝: ",nums)
#             # print(f"상태 : L: {left}, R: {right}")
#             if stored_index == len(nums) - k:
#                 return nums[stored_index]
#             elif stored_index < len(nums) - k:
#                 # print("오")
#                 left = stored_index + 1
#             else:
#                 # print(f"왼 {left-1}")
#                 right = stored_index - 1
#             # time.sleep(1)
#
#             # break


a = Solution()

nums = [3, 2, 1, 5, 6, 4]
k = 2

# nums = [3,3,3,3,3,3,3,3,3]
# k = 1

print(a.findKthLargest(nums, k))
