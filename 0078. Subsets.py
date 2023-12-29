from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(start, path):
            ans.append(path)
            for i in range(start, len(nums)):
                dfs(i + 1, path+[nums[i]])
        dfs(0,[])

        return ans


s = Solution()

nums = [1, 2, 3]
print(s.subsets(nums))
