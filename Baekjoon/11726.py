# https://www.acmicpc.net/problem/11726
# 2xn 타일링
# DP

# 0. 사용자 입력 
n = int(input()) 

# 1. 빈 리스트 생성 
dp = [0] * 1001 

# 2. 초기값 세팅 
dp[1] = 1 
dp[2] = 2 

# 3. 점화식 
for i in range(3, 1001): 
    dp[i] = dp[i-1] + dp[i-2] 
# 4. 출력 (방법의 수를 10,007로 나눈 나머지) 
print(dp[n] % 10007)