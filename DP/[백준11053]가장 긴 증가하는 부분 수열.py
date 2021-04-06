N = int(input())    # 수열 A의 크기 입력
A = list(map(int, input().split()))  # 수열 A 입력
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            # 각 단계에서 dp값을 갱신함
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
