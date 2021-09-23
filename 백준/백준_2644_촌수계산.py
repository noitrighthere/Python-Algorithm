"""
백준 2644 촌수계산
난이도: 실버2
유형: DFS/BFS
"""
from collections import deque

def BFS(dept, arr):
    count = 0
    queue = deque([[dept, count]])

    while queue:
        node = queue.popleft()
        dept = node[0]
        count = node[1]

        if dept == arr:
            return count

        if not visited[dept]:
            count += 1
            visited[dept] = True
            for e in graph[dept]:
                if not visited[e]:
                    queue.append([e, count])
                    
    return -1

n = int(input())    # n: 사람들
dept, arr = map(int, input().split())
m = int(input())    # m: 관계의 계수

# 촌수 그래프
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(BFS(dept, arr))
