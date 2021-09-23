"""
백준 1916 최소비용 구하기
난이도: 골드5
유형: 다익스트라
"""
import heapq

def dijkstra(start):
    # 그래프의 시작 정점 거리는 0으로 초기화
    distances[start] = 0
    # 모든 정점을 담을 큐 생성
    queue = []
    # 그래프의 시작 정점과 거리를 최소 힙에 넣음
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 지금까지의 거리가 발견한 거리보다 작은 경우 패스
        if distances[current_node] < current_distance:
            continue

        # 인접노드, 가중치
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            # 최단 거리를 발견했을 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

N = int(input())    # N: 도시의 개수
M = int(input())    # M: 버스의 개수

graph = [[] for _ in range(N+1)]
distances = [float('inf')] * (N+1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())

dijkstra(start)

print(distances[end])
