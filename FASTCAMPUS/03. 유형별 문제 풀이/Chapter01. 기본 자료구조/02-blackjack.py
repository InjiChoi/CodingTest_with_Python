# https://www.acmicpc.net/problem/2798
# 블랙잭
# 배열, 완전 탐색
n, m = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))

result = 0

for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            sum_val = data[i] + data[j] + data[k]
            if sum_val <= m:
                result = max(result, sum_val)
print(result)
