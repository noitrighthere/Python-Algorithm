"""
백준 10819 차이를 최대로
난이도: 실버2
유형: 완전탐색
"""
import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))

# 순열로 만듬
per = permutations(arr, N)
answer = 0

# 순열 전체를 계산하여 가장 큰 값을 찾음
for num in per:
    temp = 0
    
    for i in range(len(num)-1):
        temp += abs(num[i]-num[i+1])

    if temp > answer:
        answer = temp

print(answer)
