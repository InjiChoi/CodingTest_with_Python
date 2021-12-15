# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기
# 정렬
"""핵심 아이디어 1. 튜플 생성 (x, y)"""
"""핵심 아이디어 2. key 속성 없이 기본 정렬 라이브러리 사용하면 됨"""

N = int(input())
arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()
# arr = sorted(arr)

for a in arr:
    print(a[0], a[1])