"""
백준 3085 사탕 게임
난이도: 실버4
유형: 구현
"""
N = int(input())
board = [list(input()) for _ in range(N)]
answer = 0

def check(board):
    count = 0

    for i in range(N):
        count_row = 1
        count_col = 1

        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                count_row += 1
            else:
                count = max(count, count_row)
                count_row = 1

            if board[j][i] == board[j+1][i]:
                count_col += 1
            else:
                count = max(count, count_col)
                count_col = 1
        count = max(count, count_col, count_row)
    return count

for i in range(N):
    for j in range(N-1):
        # 인접한 위치 사탕이 다를 경우 서로 바꿈의(가로)
        if board[i][j] != board[i][j+1]:
            temp = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j+1] = temp

            answer = max(answer, check(board))

            temp = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j+1] = temp 
        # 인접한 위치의 사탕이 다를 경우 서로 바꿈(세로)
        if board[j][i] != board[j+1][i]:
            temp = board[j][i]
            board[j][i] = board[j+1][i]
            board[j+1][i] = temp

            answer = max(answer, check(board))

            temp = board[j][i]
            board[j][i] = board[j+1][i]
            board[j+1][i] = temp

print(answer)
