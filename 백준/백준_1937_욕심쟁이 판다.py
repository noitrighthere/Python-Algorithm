"""
백준 1937 욕심쟁이 판다
난이도: 골드3
유형: DFS/BFS, DP
"""
import sys
sys.setrecursionlimit(100000)

def DFS(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 영역을 벗어나지 않음
        if 0 <= nx < n and 0 <= ny < n:
            # 전에 먹었던 것 보다 더 커야 함
            if graph[x][y] < graph[nx][ny]:
                dp[x][y] = max(dp[x][y], DFS(nx, ny)+1)
                
    return dp[x][y]

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0 , 1]

max_value = 0

for i in range(n):
    for j in range(n):
        max_value = max(max_value, DFS(i, j))

print(max_value)
