from collections import deque

N = int(input())    # 정수 N 입력
queue = deque([])

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    # 가장 위에 있는 정수 삭제
    queue.popleft()
    # 제일 위에 있는 카드를 제일 아래로 옮김
    queue.append(queue[0])
    # 옮긴 카드 삭제
    queue.popleft()
    
print(queue[0])
