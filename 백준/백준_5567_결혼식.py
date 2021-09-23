"""
백준 5567 결혼식
난이도: 실버1
유형: 그래프, 그리디
"""
from collections import deque

n = int(input())    # 동기의 수
m = int(input())    # 리스트 길이

# 친구 관계 생성
graph = [[] for _ in range(n+1)]

# BFS
def BFS(v):
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for e in graph[v]:
            if not visited[e]:
                # 친구의 관계 수
                visited[e] = visited[v] + 1
                q.append(e)

    return visited

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0

visited = [0] * (n+1)
friend = BFS(1)

# 친구의 수가 3명 까지만 허용 가능
for i in friend:
    if 1 < i <= 3:
        answer += 1

print(answer)
