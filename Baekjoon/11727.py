# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2
# DP

import sys

n = int(sys.stdin.readline())

dp = [0, 1, 3]

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2]*2)

print(dp[n]%10007)