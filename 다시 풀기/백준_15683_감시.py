"""
백준 15683 감시
난이도: 골드5
유형: 구현, 완전탐색
"""
from collections import deque

def BFS(cnt):
    global visited, answer

    # 모든 cctv를 탐색했다면 사각지대 개수를 셈
    if cnt == cctv_count:
        temp = 0
        for i in range(N):
            for j in range(M):
                # 0: 사각지대
                if not graph[i][j] and not visited[i][j]:
                    temp += 1

        return temp

    x, y = cctv[cnt][0], cctv[cnt][1]

    for i in range(4):
        new_direction = []

        # 1번 cctv 일 때 : 현재 방향
        if graph[x][y] == 1:
            new_direction.append(i)
        # 2번 cctv 일 때 : 현재 방향 + 반대 방향
        elif graph[x][y] == 2:
            new_direction.append(i)
            new_direction.append((i+2) % 4)
        # 3번 cctv 일 때 : 현재 방향 + 90도 방향
        elif graph[x][y] == 3:
            new_direction.append(i)
            new_direction.append((i-1) % 4)
        # 4번 cctv 일 때 : 세 방향
        elif graph[x][y] == 4:
            new_direction.append(i)
            new_direction.append((i-1) % 4)
            new_direction.append((i+2) % 4)
        # 5번 cctv 일 때: 네 방향
        elif graph[x][y] == 5:
            new_direction.append(i)
            new_direction.append((i-1) % 4)
            new_direction.append((i+1) % 4)
            new_direction.append((i+2) % 4)

        queue = deque()

        for d in new_direction:
            nx, ny = x + dx[d], y + dy[d]

            # 방향의 끝까지 이동
            while 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 6 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                elif graph[nx][ny] == 6:
                    break

                nx += dx[d]
                ny += dy[d]

        answer = min(answer, BFS(cnt + 1))

        while queue:
            qx, qy = queue.popleft()
            if not graph[qx][qy]:
                visited[qx][qy] = False

        if graph[qx][qy] == 5:
            break
    return answer

# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctv = []   # cctv의 위치를 담는 배열
answer = 0  # 사각지대의 크기
cctv_count = 0

visited = [[False] * M for _ in range(N)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        # cctv가 위치하고 벽이 아닌 경우
        if graph[i][j] and graph[i][j] != 6:
            # cctv 위치 저장
            cctv.append((i, j))
            visited[i][j] = True
            cctv_count += 1
        else:
            answer += 1

BFS(0)
print(answer)







