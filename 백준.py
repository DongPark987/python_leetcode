import sys

# input = sys.stdin.readline
#
# N, K = map(int, input().rstrip().split())
# items = [list(map(int, input().rstrip().split())) for _ in range(N)]
#
# dp = [0 for _ in range(K + 1)]
#
# for item in items:
#     for weight in range(K, -1, -1):
#         if weight - item[0] >= 0:
#             dp[weight] = max(dp[weight], item[1] + dp[weight - item[0]])
#         else:
#             break
# print(dp[K])


def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x: x[1])
    for work in plans:
        time = work[1].split(':')
        work[1] = int(time[0]) * 60 + int(time[1])
        work[2] = int(work[2])

    next_idx = 0
    current_work = None
    for time in range(24 * 60):

        if plans[next_idx][1] == time:
            if current_work:
                current_work[2] -= 1
                if current_work[2] == 0:
                    answer.append(current_work[0])
                else:
                    stack.append([current_work[0], current_work[2]])
            else:
                if stack:
                    top = stack[-1]
                    top[1] -= 1
                    if top[1] == 0:
                        answer.append(stack.pop()[0])

            current_work = plans[next_idx]
            next_idx += 1
            if next_idx == len(plans):
                break
            continue

        if current_work:
            current_work[2] -= 1
            if current_work[2] == 0:
                answer.append(current_work[0])
                current_work = None
        else:
            if stack:
                top = stack[-1]
                top[1] -= 1
                if top[1] == 0:
                    answer.append(stack.pop()[0])
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer

data = [["a", "09:00", "10"], ["b", "09:10", "10"], ["c", "09:15", "10"], ["d", "09:30", "10"], ["e", "09:35", "10"]]
print(solution(data))