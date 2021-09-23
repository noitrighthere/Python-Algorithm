"""
백준 2589 보물섬
난이도: 골드5
유형: DFS/BFS
"""
from collections import deque

# BFS 알고리즘 사용
def BFS(x, y):
    # 덱 생성
    queue.append([x, y])

    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    count = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    count = max(count, visited[nx][ny])
                    queue.append([nx, ny])

    return count-1

# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

max_value = 0
queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            max_value = max(max_value, BFS(i, j))

print(max_value)
