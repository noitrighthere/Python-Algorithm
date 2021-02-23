from collections import deque

T = int(input())    # 테스트케이스 입력

for _ in range(T):
    
    N, M = map(int, input().split())    # N: 문서의 개수, M: 몇 번째로 인쇄되었는지 궁금한 문서
    queue = deque(map(int, input().split()))
    result = 0

    while queue:
        temp_max = max(queue)
        M -= 1
        temp = queue.popleft()

        if temp_max != temp:
            queue.append(temp)

            if M < 0:
                M = len(queue)-1

        else:
            result += 1

            if M == 1:
                print(result)
                break

    
