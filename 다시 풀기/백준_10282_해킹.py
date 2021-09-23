"""
백준 10282 해킹
난이도: 골드4
유형: 다익스트라
"""
import heapq

t = int(input())    # 테스트케이스 개수

def dijkstra(start):

    # 그래프의 시작 정점 거리는 0으로 초기화 
    distances[start] = 0
    # 모든 정점이 저장될 큐 생성
    queue = []

    # 그래프의 시작 정점과 거리를 최소힙에 넣음
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 지금까지의 거리가 발견한 거리보다 더 작다면 다음 단계 패스
        if distances[current_node] < current_distance:
            continue

        # 인접노드, 거리값
        for i in graph[current_node]:
            adjacent = i[0]
            weight = i[1]
            distance = current_distance + weight

            # 최단거리를 발견했을 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
            

for _ in range(t):
    # n: 컴퓨터 개수, d: 의존성 개수, c: 해킹당한 컴퓨터 번호
    n, d, c = map(int, input().split())
    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    # 거리 저장 배열
    distances = [float('inf')] * (n+1)    

    for _ in range(d):
        # a: 컴퓨터 a, b: 컴퓨터 b, s: 감염 시간
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    # 해킹 당한 컴퓨터부터 시작
    dijkstra(c)
    count = 0
    max_distance = 0

    # 거리에 저장이 되면 count를 하나씩 더해줌
    for i in distances:
        if i != float('inf'):
            count += 1

            # 최대 거리를 구함
            if i > max_distance:
                max_distance = i

    print(count, max_distance)
