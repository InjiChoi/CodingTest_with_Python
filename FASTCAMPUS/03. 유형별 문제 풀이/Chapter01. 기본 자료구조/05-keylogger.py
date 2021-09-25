# https://www.acmicpc.net/problem/5397
# 키로거
# 스택, 구현, 그리디

"""핵심 아이디어 : 커서 좌우로 스택 2개 활용"""
test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == "-":
            if left_stack:
                left_stack.pop()
        elif i == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))
