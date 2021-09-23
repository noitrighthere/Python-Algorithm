"""
백준 11725 트리의 부모 찾기
난이도: 실버2
유형: BFS/DFS
"""
from collections import deque

# BFS 알고리즘
def BFS():
    queue = deque()
    queue.append(1)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                queue.append(i)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
BFS()

# 2번 노드부터 순서대로 출력
for i in parent[2:]:
    print(i)
