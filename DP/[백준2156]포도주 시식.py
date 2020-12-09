n = int(input())    # 포도주의 개수
wine = [0]          # 포도주의 양
dp = [0]

for _ in range(n):
    wine.append(int(input()))

dp.append(wine[1])

# 첫 번째 잔과 두 번째 잔은 그냥 추가해도 된다.
if n > 1:
    dp.append(wine[1] + wine[2])

# 세 번째 잔부터 가장 많은 양을 마실 수 있도록 구한다.
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i]))

print(dp[n])
