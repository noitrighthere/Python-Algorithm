T = int(input())    # 테스트 케이스

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2
dp[6] = 3

for i in range(7, 101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(T):
    N = int(input())
    print(dp[N])