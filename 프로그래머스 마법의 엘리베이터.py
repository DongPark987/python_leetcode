import math
from collections import deque


def solution(storey):
    answer = 0

    while storey:
        curr = storey % 10
        storey = storey // 10
        if curr == 0:
            continue
        if curr == 5:
            if storey % 10 >= 5:
                answer += 5
                storey += 1
            else:
                answer += 5
        elif curr < 10 - curr:
            answer += curr
        else:
            answer += 10 - curr
            storey += 1
    return answer


print(solution(45))
