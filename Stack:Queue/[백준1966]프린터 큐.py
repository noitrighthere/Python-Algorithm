T = int(input())    # 테스트케이스 입력

for _ in range(T):
    N, M = map(int, input().split())    # N: 문서의 개수, M: 몇 번째로 인쇄되었는지 궁금한 문서
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    cnt = 0

    while True:
        # 현재 중요도가 가장 높은 문서가 맨 앞에 있으면
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            cnt += 1

            # 몇 번째로 인쇄되었는지 궁금한 문서일 때
            if queue[0][1] == M:
                print(cnt)
                break
            else:
                queue.pop(0)
        # 아니면 앞에 있는 문서를 빼서 뒤로 넣어줌
        else:
            queue.append(queue.pop(0))
