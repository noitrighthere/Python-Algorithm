N, K = map(int, input().split())        # N: 물품의 수, K: 버틸 수 있는 무게
dp = [[0] * (K+1) for _ in range(N+1)]  # dp 생성

for i in range(1, N+1):
    weight, value = map(int, input().split())

    # 각 무게에 대해서 매번 테이블 갱신
    for j in range(1, K+1):
        # 현재 무게보다 작은 경우 위에 있던 값을 그대로 갖고 옴
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 이전 가치와 비교해서 더 큰 것을 선택
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])
