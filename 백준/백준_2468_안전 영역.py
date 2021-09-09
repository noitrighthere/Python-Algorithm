"""
백준 2568 안전영역
난이도: 실버1
유형: BFS/DFS
"""
import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())

# 지역 입력
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# DFS 알고리즘
def DFS(x, y, limit):

    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 비의 높이 보다 높은 지점을 탐색
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                if graph[nx][ny] > limit:
                    DFS(nx, ny, limit)

for h in range(max(map(max, graph))):

    count = 0
    visited = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                DFS(i, j, h)
                count += 1

    answer = max(answer, count)

print(answer)
