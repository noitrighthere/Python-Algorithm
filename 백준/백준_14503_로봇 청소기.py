"""
백준 14503 로봇 청소기
난이도: 골드5
유형: 구현
"""
def change(d):
    # d가 0인 경우 -> 북
    if d == 0:
        return 3
    # d가 1인 경우 -> 동
    if d == 1:
        return 0
    # d가 2인 경우 -> 남
    if d == 2:
        return 1
    # d가 3인 경우 -> 서
    if d == 3:
        return 2

def solution(r, c, d):
    cnt = 1
    x = r
    y = c
    matrix[x][y] = 2

    while(1):
        empty = 0
        dc = d

        for i in range(4):
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]
            # 범위를 벗어나지 않고 청소가 필요한 부분을 탐색
            if 0 < nx <= N and 0 < ny <= M and matrix[nx][ny] == 0:
                cnt += 1
                x = nx
                y = ny
                matrix[x][y] = 2
                d = dc
                empty = 1
                break

        # 4방향 모두 탐색 후 모든 칸이 청소되어 있을 때
        if empty == 0:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1

            # 후진하는 칸이 벽이면 stop
            if matrix[x][y] == 1:
                break

    return cnt

# N: 세로 크기, M: 가로 크기
N, M = map(int, input().split())
# (r, c): 북쪽에서 떨어진 칸의 개수, 서쪽으로 부터 떨어진 칸의 개수
r, c, d = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(solution(r, c, d))
