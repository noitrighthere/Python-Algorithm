"""
백준 1464 도서관
난이도: 골드5
유형: 그리디
"""
import heapq

N, M = map(int, input().split())
arr = list(map(int, input().split()))

positive = []
negative = []

largest_distance = max(max(arr), -min(arr))

for i in arr:
    if i > 0:
        heapq.heappush(positive, -i)
    else:
        heapq.heappush(negative, i)

result = 0

while positive:
    result += heapq.heappop(positive)

    for _ in range(M-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)

    for _ in range(M-1):
        if negative:
            heapq.heappop(negative)

print(-result * 2 - largest_distance)
