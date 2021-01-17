import heapq

N = int(input())    # N 입력
card = []           # 카드를 담을 리스트

answer = 0          # 결과값

for _ in range(N):
    card.append(int(input()))

heapq.heapify(card)

while len(card) > 1:

    A = heapq.heappop(card)    # 제일 작은 수
    B = heapq.heappop(card)    # 그다음 작은 수

    heapq.heappush(card, A+B)   # 힙에 넣어줌
    answer += (A+B)
    
print(answer)

