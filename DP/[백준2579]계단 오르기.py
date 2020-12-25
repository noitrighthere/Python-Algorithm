N = int(input())                 # 계단 수 입력
temp = [0 for i in range(301)]   # 계단 점수
dp = [0 for i in range(301)]     # dp 생성

# 계단 점수 입력
for i in range(N):
    temp[i] = int(input())

dp[0] = temp[0]
dp[1] = temp[0] + temp[1]
dp[2] = max(temp[1] + temp[2], temp[0] + temp[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + temp[i-1] + temp[i], dp[i-2] + temp[i])

print(dp[N-1])
