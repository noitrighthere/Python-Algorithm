N = int(input())    # N을 입력

def solution(N):
    # N이 홀수 이면 0을 출력
    if N % 2 != 0:
        return 0

    else:
        dp = [0] * (N+1)    # dp 생성
        dp[0] = 1
        dp[2] = 3
        # dp[i] = dp[i-2]*3 + dp[i-4]*2 + ... + dp[i-i]*2
        for i in range(4, N+1):
            dp[i] = dp[i-2] * 3

            for j in range(i-4, -1, -2):
                dp[i] += dp[j] * 2

        return dp[N]

print(solution(N))
