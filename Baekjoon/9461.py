# https://www.acmicpc.net/problem/9461
# 파도반 수열
# DP

T = int(input())
arr = [0 for _ in range(T)]
dp = [0 for _ in range(101)]


for i in range(T):
    arr[i] = int(input())

for n in arr:
    for j in range(1, n+1):
        if j <= 3:
            dp[j] = 1
        elif j <= 5:
            dp[j] = 2
        else:
            dp[j] = dp[j-5] + dp[j-1]
            
    print(dp[n])