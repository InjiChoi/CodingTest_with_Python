# https://www.acmicpc.net/problem/1920
# 수 찾기
# 해시, 배열, 구현
"""핵심 아이디어1. 특정 정수의 등장 여부만을 체크"""
"""핵심 아이디어2. Python에서는 딕셔너리 자료형을 해시처럼 사용 가능"""
"""핵심 아이디어3. set(집합 => 중복 X) 자료형을 사용하여 간단하게 풀이"""

n = int(input())
array = set(map(int, input().split()))  # [3, 5, 7] => {3, 5, 7} : 중복 제거
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print("0")
    else:
        print("1")
