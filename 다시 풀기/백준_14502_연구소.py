"""
백준 14502 연구소
난이도: 골드5
유형: DFS/BFS, 구현
"""
import sys
import copy

# 넓이를 구하는 함수
def getArea(copy_graph):
    safe = 0

    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                safe += 1

    return safe

# DFS 알고리즘
def DFS(x, y, copy_graph):

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 영역을 벗어나지 않음
        if 0 <= nx < N and 0 <= ny < M:
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                DFS(nx, ny, copy_graph)

# 조합으로 벽 3개를 놓는 경우를 구함
def setWall(start, depth):
    global max_value

    # 벽 3개를 모두 놓았을 때
    if depth == 3:
        # 연구소를 복사
        copy_graph = copy.deepcopy(graph)

        for i in range(len(virus)):
            [virusX, virusY] = virus[i]
            DFS(virusX, virusY, copy_graph)

        max_value = max(max_value, getArea(copy_graph))
        return

    for i in range(start, N*M):
        x = i // M
        y = i & M

        if graph[x][y] == 0:
            graph[x][y] = 1
            setWall(i + 1, depth+1)
            graph[x][y] = 0

# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
max_value = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        # 바이러스를 발견
        if graph[i][j] == 2:
            virus.append([i, j])

setWall(0, 0)
print(max_value)
            
