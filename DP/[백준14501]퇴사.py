N = int(input())
T = []      # 상담을 완료할 때 걸리는 시간
P = []      # 받을 수 있는 금액

dp = []     # dp 생성

for i in range(N):
    temp_T, temp_P = map(int, input().split())
    T.append(temp_T)
    P.append(temp_P)
    dp.append(temp_P)

dp.append(0)

# 뒤에서 부터 dp를 구함
for i in range(N-1, -1, -1):

    # 퇴사일을 넘어가면 안됨
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[(i + T[i])])

print(dp[0])
