"""
백준 12865 평범한 배낭
난이도: 골드5
유형: DP
"""
# N: 물품의 수, K: 버틸 수 있는 무게
N, K = map(int, input().split())

# dp 생성
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    # weight: 물건의 무게, value: 물건의 가치
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        # 현재 무게보다 작은 경우 위에 있던 값을 갖고 옴
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 이전 가치와 비교해서 더 큰 것을 선택
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])
