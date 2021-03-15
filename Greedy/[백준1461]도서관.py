import heapq

N, M = map(int, input().split(' '))     # N: 책의 개수, M: 한번에 들을 수 있는 책의 수
temp = list(map(int, input().split(' ')))    # 원래 책의 위치
positive = []
negative = []
answer = 0

longest = max(max(temp), -min(temp))    # 가장 먼 책의 위치

# 최대 힙을 위해 원소를 음수로 구성
for i in temp:
    # 책의 위치가 양수인 경우
    if i > 0:
        heapq.heappush(positive, -i)
    # 책의 위치가 음수인 경우
    else:
        heapq.heappush(negative, i)

while positive:
    # 한 번에 M개씩 옮길 수 있으므로 M개씩 빼기
    answer += heapq.heappop(positive)
    for _ in range(M-1):
        if positive:
            heapq.heappop(positive)

while negative:
    
    answer += heapq.heappop(negative)
    for _ in range(M-1):
        if negative:
            heapq.heappop(negative)

# 왕복 거리 - 가장 먼 길이
print(-answer * 2 - longest)
