"""
백준 2665 미로만들기
난이도: 골드4
유형: BFS/DFS, 다익스트라
"""
import heapq

def dijkstra(x, y):
    visited[x][y] = True

    queue = []

    heapq.heappush(queue,(0, x, y))

    while queue:
        count, current_x, current_y = heapq.heappop(queue)

        # 목표지점에 도착하면 반환
        if current_x == n-1 and current_y == n-1:
            return count

        # 모든 방향을 탐색
        for i in range(4):
            nx, ny = current_x + dx[i], current_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True

                    if graph[nx][ny] == '0':
                        graph[nx][ny] = '1'
                        heapq.heappush(queue, (count+1, nx, ny))
                    else:
                        heapq.heappush(queue, (count, nx, ny))

n = int(input())    # 방의 수

graph = [[] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    graph[i] = list(input())

print(dijkstra(0, 0))
