"""
백준 4963 섬의 개수
난이도: 실버2
유형: DFS/BFS
"""
import sys
from collections import deque

# 위, 왼쪽, 아래, 오른쪽
# 왼쪽 위 대각선, 오른쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 아래 대각선
dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, -1, -1, 1, 1]

# BFS 알고리즘
def BFS(a, b):
    queue = deque()     # 덱 생성
    queue.append([a, b])
    
    while queue:
        x, y = queue.popleft()

        # 모든 방향을 조회
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나지 않으면서 섬인 곳만 확인
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                    

while True:

    # w: 너비, h: 높이
    w, h = map(int, input().split())
    answer = 0

    # w와 h가 0일 때 종료
    if w == 0 and h == 0:
        sys.exit(0)

    # 섬 그래프 생성
    graph = [list(map(int, input().split())) for _ in range(h)]

    # 섬인 곳만 둘러봄
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                BFS(i, j)
                answer += 1

    print(answer)
