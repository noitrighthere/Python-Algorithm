m = list(input())   # 행 입력
n = list(input())   # 열 입력

dp = [[0] * (len(n) + 1) for _ in range(len(m) + 1)]

# 서로 비교해서 같으면 해당 행렬 왼쪽 대각선에 +1을 함
# 같지 않으면 왼쪽과 위의 행렬 중 큰 것을 넣음
for i in range(len(m)):
    for j in range(len(n)):
        if m[i] == n[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

# 행렬의 부분 수열 중 가장 긴 것을 호출
print(dp[len(m)][len(n)])
