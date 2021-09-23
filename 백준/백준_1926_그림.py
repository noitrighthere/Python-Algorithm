"""
백준 1926 그림
난이도: 실버1
유형: BFS/DFS
"""
import sys

def BFS(x, y):
    wide = 1
    queue = [(x, y)]

    while queue:
        x, y = queue.pop()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    wide += 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return wide
    
# n: 세로, m: 가로
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)] 

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 0
wide = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            visited[i][j] = 1
            wide = max(wide, BFS(i, j))
            
print(count)
print(wide)
