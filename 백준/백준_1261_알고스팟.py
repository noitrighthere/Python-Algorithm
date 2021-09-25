"""
백준 1261 알고스팟
난이도: 골드4
유형: 다익스트라
"""
import heapq

# 다익스트라 알고리즘 사용
def dijkstra(x, y):
    visited[x][y] = True

    # 모든 정점을 담을 큐 사용
    queue = []
    # 큐에 벽을 부수는 횟수, x좌표, y좌표를 최소 힙으로 넣음
    heapq.heappush(queue, (0, x, y))

    while queue:
        count, current_x, current_y = heapq.heappop(queue)

        if current_x == N-1 and current_y == M-1:
            return count

        # 상하좌우를 탐색
        for i in range(4):
            nx, ny = current_x + dx[i], current_y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = True

                    # 1(벽)일 경우 0(벽으로 부숨)으로 바꿔줌
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        # 벽을 부순 회수를 추가해서 다시 넣어줌
                        heapq.heappush(queue,(count+1, nx, ny))
                    else:
                        heapq.heappush(queue,(count, nx, ny))

# M: 가로, N: 세로
M, N = map(int, input().split())
graph = []

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False]*M for _ in range(N)]

answer = 0

for i in range(N):
    graph.append(list(map(int, input())))

answer = dijkstra(0, 0)

print(answer)
