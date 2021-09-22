"""
백준 14716 현수막
난이도: 실버1
유형: BFS/DFS
"""
import sys
sys.setrecursionlimit(100000)

# DFS 알고리즘
def DFS(x, y):
    visited[x][y] = True

    # 모든 방향을 탐색
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        # 범위에서 벗어나지 않아야 함
        if 0 <= nx < M and 0 <= ny < N:
            # '1'인 곳을 계속해서 탐색
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                DFS(nx, ny)

# M: 세로, N: 가로
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

# 방향(대각선 포함)
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

count = 0       # 글자의 개수가 몇 개인지 확인하는 변수

# 현수막에서 '1'인 곳만을 탐색함
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            DFS(i, j)
            count += 1

print(count)
