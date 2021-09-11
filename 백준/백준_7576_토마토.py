"""
백준 7576 토마토
난이도: 실버1
유형: DFS/BFS
"""
from collections import deque

# BFS
def BFS():
    count = 0

    while queue:

        count += 1

        for _ in range(len(queue)):

            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 익지 않은 토마토를 찾아내어 익게 만듬
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        queue.append([nx, ny])

    # 익지 않은 토마토가 남았을 경우
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1

    # 모두 익었을 경우
    return count - 1

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# M: 가로, N: 세로
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

print(BFS())
            
            
            
