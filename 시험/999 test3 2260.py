from typing import List
from typing import Optional
import math
from itertools import combinations


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = math.inf
        card_dic = {}
        for i in range(len(cards)):
            if cards[i] not in card_dic:
                card_dic[cards[i]] = i
            else:
                ans = min(ans, i - card_dic[cards[i]])
                card_dic[cards[i]] = i
        if ans == math.inf:
            return -1
        return ans + 1


a = Solution()
cards = [1,0,5,3]

print(a.minimumCardPickup(cards))
