T = int(input())    # 테스트 케이스 입력

for _ in range(T):
    N, M = map(int, input().split())  # 서쪽 N, 동쪽 M 사이트 개수 입력
    answer = 1                        # 결과값

    K = M - N

    # 겹치면 안되기 때문에 순열조합을 사용 
    while M > K:
        answer *= M
        M -=1

    while N > 1:
        answer = answer // N
        N -= 1

    print(answer)
