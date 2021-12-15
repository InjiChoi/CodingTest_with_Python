# https://www.acmicpc.net/problem/1074
# 피보나치 수
# 재귀

from sys import stdin

# def solve(n, x, y):
#     global result
#     if n == 2:
#         if x == r and y == c:
#             print(result)
#             return
#         result += 1

#         if x == r and y+1 == c:
#             print(result)
#             return
#         result += 1

#         if x+1 == r and y == c:
#             print(result)
#             return
#         result += 1

#         if x+1 == r and y+1 == c:
#             print(result)
#             return
#         result += 1
#         return
    
#     # 4등분해서 반복
#     solve(n / 2, x + (n / 2), y)
#     solve(n / 2, x, y)
#     solve(n / 2, x, y + (n / 2))
#     solve(n / 2, x + (n / 2), y + (n / 2))

N, r, c = map(int, stdin.readline().split())
result = 0    
# solve(2**N, 0, 0)

def solve(n, x, y):
    global result

    if n == 2:
        for i in range(x, x+n):
            for j in range(y, y+n):
                result += 1
                if i == r and j == c:
                    print(result)
                    exit(0)
    if not(x <= r < x+n and y <=c < y+n):
        result += n**2
        return
    
    for i in range(x, x+n, n//2):
        for j in range(y, y+n, y//2):
            solve(i, j, n//2)

solve(2**N, 0, 0)