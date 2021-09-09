"""
백준 11047 동전 0
난이도: 실버2
유형: 그리디
"""
N, K = map(int, input().split())
money = []
count = 0

for _ in range(N):
    money.append(int(input()))

# 내림차순으로 정렬
money.sort(reverse=True)

for i in money:
    temp = K // i
    count += temp
    K -= temp * i

print(count)
