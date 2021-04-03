N, M = map(int, input().split())    # 성의 세로(열), 가로(행) 크기 입력
temp = []

row_count = 0       # 세로 기준
col_count = 0       # 가로 기준

# 성의 상태 입력
for _ in range(N):
    temp.append(input())

row = [0] * N
col = [0] * M

# 만약 성에 경비가 있다면 해당 포인트를 1로 지정
for i in range(N):
    for j in range(M):
        if temp[i][j] == 'X':
            row[i] = 1
            col[j] = 1

# 세로 기 필요한 경비원 탐색
for i in range(N):
    if row[i] == 0:
        row_count += 1

# 가로 기준 필요한 경비원 탐색
for j in range(M):
    if col[j] == 0:
        col_count += 1

print(max(row_count, col_count))
