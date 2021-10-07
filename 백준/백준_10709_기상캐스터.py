"""
백준 10709 기상캐스터
난이도: 실버5
유형: 구현
"""
# H: 남북방향, W: 동서방향
H, W = map(int, input().split())
# 구역 생성
board = [list(input()) for _ in range(H)]
result = [[0]*W for _ in range(H)]

for i in range(H):

    num = 1
    cloud = False   # 구름 flag

    for j in range(W):
        # 구름이 원래 없던 지역
        if not cloud and board[i][j] == '.':
            result[i][j] = -1
        # 구름이 원래 있던 지역
        elif board[i][j] == 'c':
            cloud = True
            result[i][j] = 0
            num = 1
        # 구름이 지나가는 지역
        elif cloud and board[i][j] == '.':
            result[i][j] = num
            num += 1

for i in range(len(result)):
    print(*result[i])
