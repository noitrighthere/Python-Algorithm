N, K = map(int, input().split())    # 두 정수 입력
dp = [[0]*201 for i in range(201)]  # dp 생성

# K에 상관없이 N이 1인 경우
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

# i, j가 2 이상인 경우
for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[K][N])
