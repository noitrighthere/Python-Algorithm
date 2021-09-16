"""
백준 10974 모든 순열
난이도: 실버3
유형: 완전탐색
"""
from itertools import permutations

N = int(input())
arr = [num for num in range(1, N+1)]

# 순열을 구함
per = list(permutations(arr, N))

for i in per:
    for j in i:
        print(j, end = ' ')
    print()
