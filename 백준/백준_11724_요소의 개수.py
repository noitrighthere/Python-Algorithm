"""
백준 11724 요소의 개수
난이도: 실버2
유형: DFS/BFS
"""
# DFS 방식
def DFS(v):
    visited[v] = True

    for e in graph[v]:
        if not visited[e]:
            DFS(e)

# N: 정점의 개수, M: 간선의 개수
N, M = map(int, input().split())
# 그래프 생성
graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)
answer = 0

# 그래프 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for v in range(1, N+1):
    if not visited[v]:
        DFS(v)
        answer += 1

print(answer)
