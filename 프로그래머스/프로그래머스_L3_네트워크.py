"""
프로그래머스 네트워크
난이도: LV3
유형: DFS/BFS
"""
from collections import deque

# 깊이 우선 탐색
def DFS(v, visited, n, computers):
    # 방문한 네트워크로 표시
    visited[v] = True
    
    for e in range(n):
        # e가 해당 네트워크가 아니어야 하고 컴퓨터가 서로 연결되어 있을 때
        if e != v and computers[v][e] == 1:
            # 다음 네트워크가 방문하지 않았을 때
            if not visited[e]:
                DFS(v, visited, n, computers)

# 너비 우선 탐색
def BFS(v, visited, n, computers):
    # 앞으로 찾을 네트워크
    need_visit = deque([v])

    while need_visit:
        # 해당 노드들을 꺼냄
        node = need_visit.popleft()
        if not visited[node]:
            visited[node] = True
            for e in range(n):
                if e != node and computers[node][e] == 1:
                    if not visited[e]:
                        need_visit.append(e)
                     
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for v in range(n):
        if not visited[v]:
            #DFS(v, visited, n, computers)
            BFS(v, visited, n, computers)
            answer += 1
    
    return answer
