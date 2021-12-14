# https://www.acmicpc.net/problem/2606
# 바이러스
# 그래프 이론, 그래프 탐색, DFS, BFS

com = int(input()) # 컴퓨터의 수
line = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

s = [[0]*com for i in range(com)]
visit = [0 for i in range(com)]

for i in range(line):
    a, b = map(int, input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1

# DFS 함수 정의
def dfs(v):
    visit[v] = 1 # 현재 노드는 방문 처리하기
    for i in range(com): # 현재 노드와 연결된 다른 노드 방문
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)

dfs(0)

cnt = 0
for i in range(1, com): # 1번 컴퓨터 제외하고 방문여부 검사
    if visit[i] == 1:
        cnt += 1
print(cnt)
