"""
백준 17086 아기 상어2
난이도: 실버2
유형: BFS/DFS, 완전탐색
"""
from collections import deque

def BFS(x, y):
    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True
    
    queue = deque([(x, y, 0)])
    
    while queue:
        x, y, count = queue.popleft()
        
        if graph[x][y] == 1:
            return count

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count+1))

# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향(대각선 포함)
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

answer = 0

# 0인 곳을 탐색해서 최대 크기의 안전영역을 구함
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            answer = max(answer, BFS(i, j))
            
print(answer)
