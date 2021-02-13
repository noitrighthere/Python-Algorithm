from collections import deque

N, K = map(int, input().split())    # N: 사람 수, K: 제거하는 사람
queue = deque([])                   # 데크 입력

for i in range(1, N+1):
    queue.append(i)

print('<', end='')

while queue:

    # K번째 요소를 큐의 맨 끝에 옮김
    for i in range(K-1):
        queue.append(queue[0])
        # 왼쪽의 끝값 삭제
        queue.popleft()
    # 맨 앞의 요소는 K번째 값이 됨
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')
