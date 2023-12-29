from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(start, num_list, num):
            if num == target:
                ans.append(num_list[:])
                return
            if num > target:
                return
            for i in range(start, len(candidates)):
                num_list.append(candidates[i])
                dfs(i, num_list, num + candidates[i])
                num_list.pop()

        dfs(0, [], 0)
        return ans


s = Solution()

candidates = [2, 3, 6, 7]
target = 7
print(s.combinationSum(candidates, target))
