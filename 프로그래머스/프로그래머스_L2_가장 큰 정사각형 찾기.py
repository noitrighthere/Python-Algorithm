"""
프로그래머스 가장 큰 정사각형 찾기
난이도: LV2
유형: DP
"""
def solution(board):
    answer = 1234

    n = len(board)      # 세로
    m = len(board[0])   # 가로
    
    temp = []

    for i in range(1, n):
        for j in range(1, m):
            # 표에 1인 것만 계산
            if board[i][j] == 1:
                # 위, 옆, 왼쪽 대각선 위를 계산
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    for i in board:
        for j in i:
            temp.append(j)

    answer = max(temp) ** 2
    return answer
