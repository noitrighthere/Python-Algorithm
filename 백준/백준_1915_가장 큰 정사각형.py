"""
백준 1915 가장 큰 정사각형
난이도: 골드4
유형: DP
"""
n, m = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]

# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
dp = [[0] * (m+1) for _ in range(n+1)]

# 리스트 입력
for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        arr[i+1][idx+1] = j

answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        # 배열의 값이 0이 아닌 경우
        if arr[i][j]:
            # 2차원 정사각형의 dp를 구해서 주변이 전부 1이면 2가 됨
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            answer = max(dp[i][j], answer)

# 넓이를 구함
print(answer ** 2)
