def check(temp):
    cnt1 = 0
    for i in range(8):
        for j in range(8):
            temp_i = (0 if i in [0, 2, 4, 6] else 1)
            temp_j = (0 if j in [0, 2, 4, 6] else 1)
            if (temp_i == 0 and temp_j == 0) or (temp_i ==1 and temp_j == 1):
                if temp[i][j] != "B":
                    cnt1 += 1
            if (temp_i == 0 and temp_j == 1) or (temp_i == 1 and temp_j == 0):
                if temp[i][j] != "W":
                    cnt1 += 1

    cnt2 = 0
    for i in range(8):
        for j in range(8):
            temp_i = (0 if i in [0, 2, 4, 6] else 1)
            temp_j = (0 if j in [0, 2, 4, 6] else 1)
            if (temp_i == 0 and temp_j == 0) or (temp_i == 1 and temp_j == 1):
                if temp[i][j] != "W":
                    cnt2 += 1
            if (temp_i == 0 and temp_j == 1) or (temp_i == 1 and temp_j == 0):
                if temp[i][j] != "B":
                    cnt2 += 1

    return min(cnt1, cnt2)

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
temp = list()

for i in range(N-7):
    for j in range(M-7):
        ex = [z[(0+j):(8+j)] for z in chess[(0+i):(8+i)]]
        temp.append(check(ex))

print(min(temp))
