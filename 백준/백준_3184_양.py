"""
백준 3184 양
난이도: 실버2
유형: BFS/DFS
"""
from collections import deque

def BFS(x, y):
    queue = deque([(x, y)])
    o_temp, v_temp = 0, 0

    # 울타리 안에 있는 양과 늑대의 수를 셈
    while queue:
        x, y = queue.popleft()

        if graph[x][y] == 'v':
            v_temp += 1
        elif graph[x][y] == 'o':
            o_temp += 1

        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    # 늑대가 양의 수보다 같거나 많을 때: 양은 다 죽음
    if o_temp <= v_temp:
        o_temp = 0
    # 그렇지 않으면 늑대들이 쫓겨남
    else:
        v_temp = 0

    return o_temp, v_temp

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

o_count, v_count = 0, 0

for i in range(R):
    for j in range(C):
        # 울타리안에 양이나 늑대가 있는 경우
        if graph[i][j] == 'v' or graph[i][j] == 'o':
            if not visited[i][j]:
                visited[i][j] = True
                o_temp, v_temp = BFS(i, j)
                o_count += o_temp
                v_count += v_temp

print(o_count, v_count)
