import bisect
import copy
from typing import List
from collections import deque


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            mid = (left + right) // 2
            pivot = nums[mid]
            nums[mid], nums[right] = nums[right], nums[mid]
            back_right = right
            right = right - 1

            while True:
                print(nums)
                while nums[left] < pivot:
                    if left < len(nums):
                        left = left + 1
                    else:
                        break
                while nums[right] > pivot:
                    print(right)
                    if right > 0:
                        right = right - 1
                    else:
                        break
                if left >= right:
                    break

            print(right, back_right)
            nums[right], nums[back_right] = nums[back_right], nums[right]
            print(nums)


        pass


a = Solution()

nums = [3, 2, 1, 5, 6, 4]
k = 2

print(a.findKthLargest(nums, k))
