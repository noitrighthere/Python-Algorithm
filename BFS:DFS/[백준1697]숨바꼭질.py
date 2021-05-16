from collections import deque

limit = 100001
N, K = map(int, input().split()) # N: 수빈이가 있는 위치, M: 동생이 있는 위치

arr = [0] * limit

def BFS(arr, N, K):
    need_visit = deque()
    need_visit.append(N)    # 수빈이가 있는 현재 위치 추가

    while need_visit:
        node = need_visit.popleft()

        # 동생이 있는 위치면 현재 위치를 반환
        if node == K:
            return (arr[node])

        for i in (node+1, node-1, node*2):
            if (0 <= i < limit) and arr[i] == 0:
                arr[i] = arr[node] + 1
                need_visit.append(i)

print(BFS(arr, N, K))
