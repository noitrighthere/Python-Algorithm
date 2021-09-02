"""
백준 9251 LCS
난이도: 골드5
유형: DP
"""
# 두 문자열 입력
a = input()
b = input()

# dp 생성
dp = [[0] * (len(b) + 1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        # 공통 부분이 있을 경우
        # dp = dp[i-1][j-1] + 1
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 공통 부분이 아닐 경우
        # dp = max(dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(a)][len(b)])
