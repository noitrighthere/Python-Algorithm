"""
백준 1057 토너먼트
난이도: 실버3
유형: 완전탐색
"""
import math

N, a, b = map(int, input().split())
answer = 0

while a != b:

    a, b = math.ceil(a/2), math.ceil(b/2)
    answer += 1

print(answer)
