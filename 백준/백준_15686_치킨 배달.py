"""
백준 15686 치킨 배달
난이도: 골드5
유형: 구현, 완전탐색
"""
from itertools import combinations

# M개의 치킨집
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

home = []       # 집의 위치를 담을 배열
chicken = []    # 치킨집의 위치를 담을 배열

for i in range(N):
    for j in range(N):
        # 집일 경우
        if graph[i][j] == 1:
            home.append((i, j))
        # 치킨집일 경우
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 치킨집의 위치를 조합을 통해 모두 나타냄
combi = list(combinations(chicken, M))
answer = [0] * len(combi)

# 집의 위치에서 치킨집의 거리를 계산 후 가장 작은 값을 더함
for i in home:
    for j in range(len(combi)):
        min_result = 100
        for k in combi[j]:
            temp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            min_result = min(min_result, temp)
        answer[j] += min_result

print(min(answer))
