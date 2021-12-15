# https://www.acmicpc.net/problem/2747
# 피보나치 수
# 재귀

n = int(input())
a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)



### 실패 코드 예시 (시간 초과)
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(n))