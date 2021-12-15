# https://www.acmicpc.net/problem/10814
# 나이순 정렬
# 정렬
"""핵심 아이디어 1. 튜플 생성 (나이, 이름)"""
"""핵심 아이디어 2. 나이가 같으면 가입한 순으로 출력"""

N = int(input())
arr = list()

for i in range(N):
    data = input().split(' ')
    arr.append((int(data[0]), data[1])) # 튜플로 저장

arr = sorted(arr, key=lambda x: x[0]) 
# 정렬된 결과 반환
# 나머지 원소는 stable 하므로 먼저 입력된 순서가 지켜짐

for a in arr:
    print(a[0], a[1])