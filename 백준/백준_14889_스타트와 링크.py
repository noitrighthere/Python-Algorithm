"""
백준 14889 스타트와 링크
난이도: 실버3
유형: 완전탐색
"""
import sys
from itertools import combinations

N = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
team = []

# 사람들을 조합으로 나눔
combi = list(combinations(members, N//2))

for i in combi:
    team.append(i)

# 정답
answer = 10000

for i in range(len(team)//2):

    start = team[i]

    # 스타트 능력치
    start_ability = 0

    for j in range(N//2):
        member = start[j]
        for k in start:
            start_ability += graph[member][k]

    link = team[-i-1]
    link_ability = 0

    # 링크 능력치
    for j in range(N//2):
        member = link[j]
        for k in link:
            link_ability += graph[member][k]

    answer = min(answer, abs(start_ability - link_ability))

print(answer)
