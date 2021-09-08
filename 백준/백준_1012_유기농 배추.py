"""
백준 1012 유기농 배추
난이도: 실버2
유형: DFS/BFS
"""
import sys
sys.setrecursionlimit(100000)

# DFS
def DFS(x, y):

    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] and not visited[nx][ny]:
                DFS(nx, ny)

# 테스트 케이스
T = int(input())

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(T):
    # M: 가로길이, N: 세로길이, K: 배추 위치의 개수
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    result = 0

    for _ in range(K):
        # x좌표, y좌표 입력
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            # 아직 방문을 하지 않은 곳, 배추가 심어져 있는 땅일 경우 수행
            if graph[i][j] and not visited[i][j]:
                DFS(i, j)
                result += 1

    print(result)
