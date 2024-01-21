from collections import deque
import math

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(sequence):
    answer = 0
    e_list = list(enumerate(sequence))
    seq1 = list(map(lambda pair: pair[1] if pair[0] % 2 != 0 else pair[1] * -1, e_list))
    seq2 = list(map(lambda pair: pair[1] if pair[0] % 2 == 0 else pair[1] * -1, e_list))

    dq = deque()
    curSum = 0
    for i in seq1:
        while dq and curSum < 0:
            curSum -= dq.popleft()
        curSum += i
        answer = max(answer, curSum)
        dq.append(i)

    dq.clear()
    curSum = 0
    for i in seq2:
        while dq and curSum < 0:
            curSum -= dq.popleft()
        curSum += i
        answer = max(answer, curSum)
        dq.append(i)

    return answer


data = [2, 3, -6, 1, 3, -1, 2, 4]

print(solution(data))
