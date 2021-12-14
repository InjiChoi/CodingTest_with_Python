# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
# DP

import sys

# 테스트케이스 개수 입력
T = int(sys.stdin.readline())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2 # 1+1, 2
    elif n == 3:
        return 4 # 1+1+1, 1+2, 2+1, 3
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(T):
    n = int(sys.stdin.readline())
    print(sol(n))