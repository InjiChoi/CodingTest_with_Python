# https://www.acmicpc.net/problem/1654
# 랜선 자르기
# 이분 탐색, 매개 변수 탐색

from sys import stdin

# K: 이미 가지고 있는 랜선의 개수, N: 필요한 랜선의 개수
K, N = map(int, stdin.readline().split(' '))
arr = [int(stdin.readline()) for _ in range(K)]

start, end = 1, max(arr)

# 이분탐색 시작
while start <= end:
    mid = (start + end) // 2
    lans = sum([(i // mid) for i in arr]) # 잘라낸 랜선 개수
    if lans >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)