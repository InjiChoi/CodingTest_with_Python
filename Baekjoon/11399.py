# https://www.acmicpc.net/problem/11399
# ATM
# 그리디, 정렬


# 사람의 수 입력
N = int(input())
# 각 사람이 돈을 인출하는데 걸리는 시간 입력
times = list(map(int, input().split()))
times.sort()

total = 0

for i in range(N):
    for j in range(i+1):
        total += times[j]

print(total)