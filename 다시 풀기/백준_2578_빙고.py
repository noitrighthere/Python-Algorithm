"""
백준 2578 빙고
난이도: 실버5
유형: 구현
"""
def isBingo():
    # 가로 체크
    for i in range(5):
        if all(check[i]):
            row_check[i] = True

    # 세로 체크
    for i in range(5):
        tmp = list()
        for j in range(5):
            tmp.append(check[j][i])

        if all(tmp):
            col_check[i] = True

    temp_right = list()
    temp_left = list()

    # 대각선 체크
    for i in range(5):
        # 오른쪽 대각선
        temp_right.append(check[i][i])
        # 왼쪽 대각선
        temp_left.append(check[i][4-i])

    if all(temp_right):
        dia_check[0] = True
    if all(temp_left):
        dia_check[1] = True

def count():
    count = 0

    for i in range(5):
        if row_check[i]:
            count += 1
        if col_check[i]:
            count += 1
    for i in range(2):
        if dia_check[i]:
            count += 1

    return count

# 빙고판 생성
board = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 번호
temp = list()

for _ in range(5):
    temp.extend(list(map(int, input().split())))

check = [[False] * 5 for _ in range(5)]
row_check = [False] * 5     # 가로
col_check = [False] * 5     # 세로
dia_check = [False] * 2

for i in range(len(temp)):
    for j in range(5):
        # 번호가 빙고에 있을 경우
        if temp[i] in board[j]:
            x = j

    y = board[x].index(temp[i])
    # 해당 위치를 True로 바꿈
    check[x][y] = True
    # 빙고인지 체크
    isBingo()

    if count() >= 3:
        print(i+1)
        break
