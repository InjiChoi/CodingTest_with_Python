# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3
# 정렬
"""핵심 아이디어 1. 데이터 개수가 많으므로 시간 복잡도 O(N) 알고리즘 사용"""
"""핵심 아이디어 2. 1~10000보다 작거나 같은 자연수이므로 계수 정렬(Counting Sort) 이용"""

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N):
    data = int(sys.stdin.readline())
    arr[data] += 1 # 데이터 값 == 인덱스 이므로

for i in range(10001): # 1~10000
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)