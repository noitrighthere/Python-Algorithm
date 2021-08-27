"""
프로그래머스 여행경로
난이도: LV3
유형: DFS/BFS
"""
from collections import defaultdict

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
           ["ATL","SFO"]]
        
def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for dept, arr in sorted(tickets):
        graph[dept].append(arr)

    def DFS(dept):
        while graph[dept]:
            DFS(graph[dept].pop(0))
        answer.append(dept)

    DFS("ICN")

    return answer[::-1]

print(solution2(tickets))
