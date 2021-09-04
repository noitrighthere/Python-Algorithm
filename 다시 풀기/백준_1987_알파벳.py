"""
백준 1987 알파벳
난이도: 골드4
유형: BFS/DFS
"""
from collections import deque
import sys
sys.setrecursionlimit(100000)

def DFS(a, b, ans):
    global answer

    answer = max(answer, ans)
    x = a
    y = b

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[ord(graph[nx][ny]) - 65]:
                visited[ord(graph[nx][ny]) - 65] = 1
                DFS(nx, ny, ans+1)
                visited[ord(graph[nx][ny]) - 65] = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# R: 세로, C: 가로
R, C = map(int, input().split())

# 그래프 입력
graph = [list(input()) for _ in range(R)]
visited = [0] * 26
visited[ord(graph[0][0]) - 65] = 1
answer = 1

DFS(0, 0, 1)
print(answer)
