# https://www.acmicpc.net/problem/2750
# 수 정렬하기
# 정렬
"""핵심 아이디어. 데이터 개수가 1000개 이하이므로 기본 정렬 알고리즘 사용"""

N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)

arr.sort() # O(nlogn)

# for i in range(N):
#     minimum = i
#     for j in range(i+1, N):
#         if arr[minimum] > arr[j]:
#             minimum = j
#     arr[i], arr[minimum] = arr[minimum], arr[i]

for i in arr:
    print(i)