"""
프로그래머스 정수 삼각형
난이도: LV3
유형: DP
"""
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    # dp 생성
    dp = [[0 for _ in range(len(triangle)+1)] for _ in range(len(triangle)+1)]

    for i in range(1, len(triangle)+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j-1]

    answer = max(dp[-1])
    return answer

print(solution(triangle))
