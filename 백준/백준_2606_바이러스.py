"""
백준 2606 바이러스
난이도: 실버3
유형: DFS/BFS
"""
n = int(input())    # 컴퓨터의 수
m = int(input())    # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]    # 네트워크
count = 0

# 네트워크 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count

    visited[v] = True

    for e in graph[v]:
        if not visited[e]:
            count += 1
            dfs(e)

visited = [False] * (n+1)
dfs(1)
print(count)
