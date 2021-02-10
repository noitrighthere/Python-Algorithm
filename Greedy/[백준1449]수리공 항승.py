N, L = map(int, input().split())       # N: 물이 새는 곳의 개수, L: 테이프 길이
temp = list(map(int, input().split())) # 물이 새는 곳의 위치
answer = 1      # 최소한의 테이프의 수

temp.sort()
L_temp = temp[0]+(L-1)

for i in range(1, N):

    if temp[i] <= L_temp:
        continue
    answer += 1
    L_temp = temp[i] + (L-1)

print(answer)
