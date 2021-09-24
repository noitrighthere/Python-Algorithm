"""
프로그래머스 게임 맵 최단거리
난이도: LV2
유형: BFS/DFS
"""
from collections import deque

def solution(maps):
    
    answer = 0
    # 방향
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    r = len(maps)
    c = len(maps[0])
    
    visited = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append((0, 0))

    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    answer = visited[-1][-1]
                    
    return answer
