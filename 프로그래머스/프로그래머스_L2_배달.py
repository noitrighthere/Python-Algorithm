"""
프로그래머스 배달
난이도: LV2
유형: 다익스트라
"""
import heapq

def solution(N, road, K):
    answer = 0

    def dijsktra(start):
        distances[start] = 0

        queue = []

        heapq.heappush(queue, (distances[start], start))

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            # 지금까지의 거리가 발견한 거리보다 작다면 패스
            if distances[current_node] < current_distance:
                continue

            # 인접노드, 가중치
            for adjacent, weight in graph[current_node]:

                distance = current_distance + weight

                # 최단 거리를 발견했을 경우
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, (distance, adjacent))
                    

    distances = [float('inf')] * (N+1)
    graph = [[] for _ in range(N+1)]

    # a: 마을, b: 마을, c: 도로를 지나는데 걸리는 시간
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 1번 마을부터 시작
    dijsktra(1)

    for i in distances[1:]:
        if i <= K:
            answer += 1
    
    return answer
