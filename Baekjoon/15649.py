# https://www.acmicpc.net/problem/15649
# N과 M (1)
# 백트래킹, DFS

N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]
visited = [0 for _ in range(N)]
answer_list = []

def dfs(cnt):
    if (cnt == M): # 정답 배열 길이가 M 일 경우 출력
        print(*answer_list)
        return
    
    for i in range(0, N):
        if visited[i]:
            continue # 이미 방문 했으면 pass

        visited[i] = 1 # 방문 체크
        answer_list.append(numbers[i])
        dfs(cnt+1) # 재귀 호출
        answer_list.pop()
        # print(answer_list)
        visited[i] = 0 # 재귀 종료 후 원상태로 복구

dfs(0)


# from itertools import permutations

# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)
# for i in P:
#     print(' '.join(map(str, i)))