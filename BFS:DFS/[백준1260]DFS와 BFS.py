from collections import deque

def dfs(node):
    print(node, end = '')
    visited[node] = True

    for i in arr[node]:
        if not(visited[i]):
            dfs(i)

def bfs(node):
    need_visit = deque([node])

    while need_visit:
        node = need_visit.popleft()
        
        if not(visited[node]):
            visited[node] = True
            print(node, end = '')
            
            for i in arr[node]:
                if not visited[i]:
                    need_visit.append(i)

N, M, V = map(int, input().split())     # N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점
arr = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(x)
    arr[y].append(y)

print(arr)

for i in arr:
    i.sort()

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
    
