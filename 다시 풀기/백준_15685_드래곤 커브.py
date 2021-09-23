"""
백준 15685 드래곤 커브
난이도: 골드4
유형: 구현
"""
max_int = 101
end_x = 0
end_y = 0
answer = 0
N = int(input())    # 드래곤 커브의 개수

# [동, 북, 서, 남]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dragon_curve = []
matrix = [[False] * max_int for _ in range(max_int)]

def generation():
    for i in range(len(dragon_curve)-1, -1, -1):
        direction = (dragon_curve[i] + 1) % 4

        global end_x, end_y
        end_x = end_x + dx[direction]
        end_y = end_y + dy[direction]

        matrix[end_x][end_y] = True

        dragon_curve.append(direction)

for _ in range(N):
    # x, y: 드래곤 커브의 시작점
    # d: 시작 방향
    # g: 세대
    y, x, d, g = map(int, input().split())

    dragon_curve.clear()

    end_x = x
    end_y = y

    matrix[end_x][end_y] = True

    end_x = x + dx[d]
    end_y = y + dy[d]

    matrix[end_x][end_y] = True

    dragon_curve.append(d)

    for _ in range(g):
        generation()

for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i+1][j] and matrix[i][j+1] and matrix[i+1][j+1]:
            answer += 1

print(answer)
