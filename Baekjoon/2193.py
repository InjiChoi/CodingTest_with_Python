# https://www.acmicpc.net/problem/2193
# 이친수
# DP

N = int(input()) # 자리수 입력

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    elif i ==2:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])