from collections import deque
import math

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx = n
    p_idx = n
    while True:
        tmpCap = cap
        curr = -1
        for idx in range(d_idx - 1, -1, -1):
            if deliveries[idx] != 0:
                curr = max(curr, idx + 1)
                tmpCap -= deliveries[idx]
                if tmpCap <= 0:
                    deliveries[idx] = -tmpCap
                    break
                else:
                    deliveries[idx] = 0
        d_idx = curr
        tmpCap = cap
        curr = -1
        for idx in range(p_idx - 1, -1, -1):
            if pickups[idx] != 0:
                curr = max(curr, idx + 1)
                tmpCap -= pickups[idx]
                if tmpCap <= 0:
                    pickups[idx] = -tmpCap
                    break
                else:
                    pickups[idx] = 0
        p_idx = curr
        curr = max(p_idx, d_idx)
        if curr == -1:
            break
        answer += (curr * 2)


    return answer


data = [2, 3, -6, 1, 3, -1, 2, 4]

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
