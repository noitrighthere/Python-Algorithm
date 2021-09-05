"""
백준 2167 2차원 배열의 합
난이도: 브론즈1
유형: DP
"""
# N, M: 배열의 크기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp 생성
# dp[i][j] = arr[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# K: 합을 구할 부분의 개수
K = int(input())

for _ in range(K):
    # (i, j) -> (x, y)
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
