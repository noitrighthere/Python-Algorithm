"""
백준 1753 최단경로
난이도: 골드5
유형: 다익스트라
"""
import heapq

# 다익스트라 알고리즘
def dijkstra(start):
    # 그래프의 시작 정점 거리는 0으로 초기화
    distances[start] = 0
    
    # 모든 정점이 저장될 큐 생성
    queue = []

    # 그래프의 시작 정점과 거리를 최소힙에 넣음
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 지금까지의 거리가 발견한 거리보다 작은 경우 패스
        if distances[current_node] < current_distance:
            continue

        # 인접노드, 가중치
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            # 최단거리를 발견했을 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# K: 정점의 시작 번호
K = int(input())

graph = [[] for _ in range(V+1)]
distances = [float('inf')] * (V+1)

for _ in range(E):
    # u: 정점, v: 정점, w: 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in distances[1:]:
    if i == float('inf'):
        print("INF")
    else:
        print(i)
