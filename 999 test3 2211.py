from typing import List
from typing import Optional
import math
from itertools import combinations


class Solution:
    def countCollisions(self, directions: str) -> int:
        carCnt = len(directions)
        collision = 0
        carStack = []
        isStop = False
        for car in directions:

            if not carStack:
                if car != 'S':
                    carStack.append(car)
                else:
                    isStop = True
                continue
            if carStack[-1] == car:
                carStack.append(car)
            else:
                if car == 'S':
                    if carStack[-1] == 'R':
                        collision += len(carStack)
                        carStack = []
                    elif carStack[-1] == 'L':
                        if isStop:
                            collision += len(carStack)
                        carStack = []

                elif car == 'L':
                    if carStack[-1] == 'R':
                        collision += len(carStack) + 1
                        carStack = []
                else:
                    if carStack[-1] == 'L':
                        if isStop:
                            collision += len(carStack)
                    carStack = ['R']
                isStop = True
        if carStack:
            if isStop and carStack[-1] == 'L':
                collision += len(carStack)
        return collision


a = Solution()
directions = "SSLSRSSSSLRRRSLSSRRRLRLRSLRSSSSL"

print(a.countCollisions(directions))
