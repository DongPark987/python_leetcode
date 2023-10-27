from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        Width = len(height)
        Max_height = max(height)
        print(Width, Max_height)
        flood_cnt = 0
        # 좌측 제거, 우측 제거
        for k in range(2):
            for i in range(1, Max_height + 1):
                if height[0] < i:
                    for h in height:
                        if h < i:
                            flood_cnt = flood_cnt + 1
                        else:
                            break
            height.reverse()

        return Width * Max_height - flood_cnt - sum(height)


a = Solution()

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(a.trap(height))
