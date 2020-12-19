arr = [[0] * 15 for _ in range(5)]    # 문자열 생성


# 한 줄 마다 글자 입력
for i in range(5):
    c = list(input())

    for j in range(len(c)):
        arr[i][j] = c[j]
        
# 세로로 읽음
for i in range(15):
    for j in range(5):

        # 해당 자리의 글자가 없으면, 읽지 않고 다음 글자를 읽음
        if arr[j][i] == 0:
            continue;
        else:
            print(arr[j][i], end = "")
