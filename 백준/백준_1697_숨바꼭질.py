"""
백준 1697 숨바꼭질
난이도: 실버1
유형: DFS/BFS
"""
from collections import deque

N, K = map(int, input().split())

MAX = 100001
graph = [0] * MAX

def BFS():

    q = deque([N])

    while q:

        v = q.popleft()

        if v == K:
            return graph[v]

        for e in (v-1, v+1, v*2):
            if 0 <= e < MAX and not graph[e]:
                graph[e] = graph[v] + 1
                q.append(e)

print(BFS())
