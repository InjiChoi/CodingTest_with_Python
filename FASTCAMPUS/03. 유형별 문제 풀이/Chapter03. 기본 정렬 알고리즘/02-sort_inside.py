# https://www.acmicpc.net/problem/1427
# 소트인사이드
# 정렬, 배열
"""핵심 아이디어. 9부터 0까지 차례대로 확인 후 각 숫자의 개수 계산해서 출력하기"""

numbers = input()

for i in range(9, -1, -1):
    for j in numbers:
        if int(j) == i:
            print(i, end='')