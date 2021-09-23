import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    
    p = sys.stdin.readline()        # 수행할 함수
    n = int(sys.stdin.readline())   # 배열에 들어있는 수의 개수
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")    # 배열

    queue = deque(arr)              # 덱 생성

    reverse_flag = 0                # R 플래그
    error_flag = 0                  # 에러 플래그

    if n == 0:
        queue = []

    for cmd in p:
        if cmd == "R":
            reverse_flag += 1
        elif cmd == "D":
            if len(queue) < 1:
                error_flag = 1
                print("error")
                break
            else:
                if reverse_flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if error_flag == 0:
        if reverse_flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
        
    
