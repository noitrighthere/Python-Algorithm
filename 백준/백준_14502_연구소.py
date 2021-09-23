"""
백준 14502 연구소
난이도: 골드5
유형: DFS/BFS, 완전탐색
"""
import sys
import copy
from itertools import combinations
sys.setrecursionlimit(100000)

# DFS 알고리즘
def DFS(x, y):
    # 바이러스에 걸림
    copy_graph[x][y] = 2

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if copy_graph[nx][ny] == 0:
                DFS(nx, ny)

# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
zero = []

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        # 바이러스가 있는 곳의 위치를 저장
        if graph[i][j] == 2:
            virus.append([i, j])
        # 아직 바이러스가 안 걸린 곳을 저장
        elif graph[i][j] == 0:
            zero.append([i, j])

# 벽이 세워질 수 있는 조합
combi = combinations(zero, 3)

# 안전 구역의 수를 저장할 배열
safety_zone = []

for com in combi:
    # 그래프를 깊은 복사함
    copy_graph = copy.deepcopy(graph)

    # 벽을 세움
    copy_graph[com[0][0]][com[0][1]] = 1
    copy_graph[com[1][0]][com[1][1]] = 1
    copy_graph[com[2][0]][com[2][1]] = 1

    # 바이러스가 퍼짐
    for vi in virus:
        DFS(vi[0], vi[1])

    safe_count = 0

    # 안전구역을 카운트
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                safe_count += 1

    safety_zone.append(safe_count)

print(max(safety_zone))
