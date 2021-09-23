"""
백준 2636 치즈
난이도: 골드5
유형: 구현
"""
from collections import deque

def BFS():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    queue = deque([(0, 0)])
    # 치즈가 몇개인지 세는 변수
    count = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위에 벗어나지 않음
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    # 0인 경우 해당 방문을 True로 해놓음
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                    # 치즈가 존재하는 구역인 경우 치즈의 개수를 세고 0으로 만듬
                    elif graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        count += 1
                        visited[nx][ny] = True

    cheese.append(count)
    return count
            
# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cheese = []

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 시간을 세는 변수
time = 0

while True:
    time += 1
    count = BFS()

    if count == 0:
        break

print(time - 1)
print(cheese[-2])
