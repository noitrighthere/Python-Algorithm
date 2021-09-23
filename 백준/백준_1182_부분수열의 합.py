"""
백준 1182 부분수열의 합
난이도: 실버2
유형: 완전탐색
"""
from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

for i in range(1, N+1):
    # 부분수열을 구함
    sub = list(combinations(arr, i))

    for j in sub:
        if sum(j) == S:
            count += 1

print(count)
