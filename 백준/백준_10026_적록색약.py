"""
백준 10026 적록색약
난이도: 골드5
유형: BFS/DFS
"""
import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
# 구역 입력
graph = [list(input()) for _ in range(N)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# DFS 알고리즘
def DFS(x, y, color):
    
    visited[x][y] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                # 해당 색을 재귀적으로 계속 찾아나감
                if graph[nx][ny] == color:
                    DFS(nx, ny, color)
# case 1. 정상인
cnt = 0
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j, graph[i][j])
            cnt += 1

print(cnt, end = ' ')

# case 2. 적록색맹
cnt = 0
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 적록색맹이므로 'G'를 'R'로 혹은 'R'을 'G'로 만들어줌
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j, graph[i][j])
            cnt += 1

print(cnt)
