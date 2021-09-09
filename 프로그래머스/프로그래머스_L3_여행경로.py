"""
프로그래머스 여행경로
난이도: LV3
유형: DFS/BFS
"""
from collections import defaultdict
        
def solution(tickets):
    answer = []
    graph = defaultdict(list)

    # 출발지 : 도착지 딕셔너리로 만듬(알파벳순)
    for dept, arr in sorted(tickets):
        graph[dept].append(arr)

    # DFS 방식
    def DFS(dept):
        while graph[dept]:
            DFS(graph[dept].pop(0))
        answer.append(dept)

    DFS("ICN")

    return answer[::-1]
