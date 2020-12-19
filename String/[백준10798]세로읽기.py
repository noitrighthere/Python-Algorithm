arr = [[0] * 15 for _ in range(5)]    # 문자열 생성


for i in range(5):
    c = list(input())

    for j in range(len(c)):
        arr[i][j] = c[j]

for i in range(15):
    for j in range(5):
        if arr[j][i] == 0:
            continue;
        else:
            print(arr[j][i], end = "")
