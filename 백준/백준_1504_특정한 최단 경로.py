"""
백준 1504 특정한 최단 경로
난이도: 골드4
유형: 다익스트라
"""
import heapq

def dijkstra(start):
    distances = [float('inf')] * (N+1)
    # 그래프의 시작 정점 거리를 0으로 초기화
    distances[start] = 0
    # 정점이 저장될 큐 생성
    queue = []

    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 지금까지의 거리가 발견한 거리보다 더 작다면 패스
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            # 최단거리를 발견했을 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

# N: 정점의 개수, E: 간선의 개수
N, E = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(E):
    # a: 정점, b: 정점, c: 거리
    a, b, c = map(int, input().split())

    # 그래프 생성
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

temp = dijkstra(1)
temp_v1 = dijkstra(v1)
temp_v2 = dijkstra(v2)

v1_path = temp[v1] + temp_v1[v2] + temp_v2[N]
v2_path = temp[v2] + temp_v2[v1] + temp_v1[N]

answer = min(v1_path, v2_path)

if answer < float('inf'):
    print(answer)
else:
    print(-1)
