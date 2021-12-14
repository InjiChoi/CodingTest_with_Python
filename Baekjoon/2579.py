# https://www.acmicpc.net/problem/2579
# 계단 오르기
# DP
from sys import stdin

N = int(stdin.readline()) # 계단 수 입력
scores = [0 for _ in range(N)]
for i in range(N):
    scores[i] = int(stdin.readline())

if N == 1:
    print(scores[N-1])
elif N == 2:
    print(max(scores[0] + scores[1], scores[1]))
elif N == 3:
    print(max(scores[0] + scores[2], scores[1] + scores[2]))
else:
    dp = []
    dp.append(scores[0])
    dp.append(max(scores[0] + scores[1], scores[1]))
    dp.append(max(scores[0] + scores[2], scores[1] + scores[2]))

    for i in range(3, N):
        dp.append(max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i]))

    print(dp[N-1])