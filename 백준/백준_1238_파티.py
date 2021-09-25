"""
백준 1238 파티
난이도: 골드3
유형: 다익스트라
"""
import heapq

def dijkstra(start):
    distances = [float('inf')] * (N+1)
    # 시작 정점의 거리를 0으로 초기화
    distances[start] = 0
    # 모든 정점을 담을 큐 생성
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 지금까지의 거리가 새로 발견한 거리보다 작은 경우 패스
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            # 최단 거리를 발견했을 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

# N: 학생 수, M: 도로, X: 목적지
N, M, X = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
answer = [0]*(N+1)

for _ in range(M):
    # A: 도시, B: 도시, T: 소요시간
    A, B, T = map(int, input().split())
    graph[A].append((B, T))

# 오고 가는 길을 모두 구함
for i in range(1, N+1):
    temp = dijkstra(i)
    answer[i] = temp[X]
    temp2 = dijkstra(X)
    answer[i] += temp2[i]

# 가장 오래 걸리는 소요시간 출력
print(max(answer))
