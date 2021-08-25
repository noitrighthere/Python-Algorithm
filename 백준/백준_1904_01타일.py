"""
백준 1904 01타일
난이도: 실버3
유형: DP
"""
N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])
