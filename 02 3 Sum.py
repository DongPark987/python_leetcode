from typing import List


class Solution:
    def samSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        left = 0
        right = len(nums) - 1
        tmp_result = set()
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if -(nums[left] + nums[right]) in d and d[-(nums[left] + nums[right])]!=left and d[-(nums[left] + nums[right])]!=right:
                    tmp_list = [nums[left], -(nums[left] + nums[right]), nums[right]]
                    tmp_list.sort()
                    tmp_tuple = tuple(tmp_list)
                    tmp_result.add(tmp_tuple)
        result = []
        for i in tmp_result:
            result.append(list(i))
        return result


a = Solution()

nums = [-1, 0, 1, 2, -1, -4]
print(a.samSum(nums))
