N = int(input())    # 집의 수 N
RGB = []
dp = []

for i in range(N):
    r, g, b = map(int, input().split(' '))
    RGB.append((r, g, b))
    
dp.append(RGB[0])

for i in range(1, N):
    tmp = []
    tmp.append(min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]) # R을 선택
    tmp.append(min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]) # G를 선택
    tmp.append(min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]) # B를 선택
    
    dp.append(tmp)
    
print(min(dp[N-1]))