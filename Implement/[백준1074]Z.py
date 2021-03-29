def func(n, x, y):
    global answer

    # 크기가 2 x 2인 한수에 대해서 종결조건을 설정
    if n == 2:
        # 왼쪽 위
        if x == r and y == c:
            print(answer)
            return
        answer += 1

        # 오른쪽 위
        if x == r and y + 1 == c:
            print(answer)
            return
        answer += 1

        # 왼쪽 아래
        if x + 1 == r and y == c:
            print(answer)
            return
        answer += 1

        # 오른쪽 아래
        if x + 1 == r and y + 1 == c:
            print(answer)
            return
        answer += 1

    else:
        # 지그재그 형태로 4등분하여 각각 재귀함수를 호출함
        func(n // 2, x, y)
        func(n // 2, x, y + n // 2)
        func(n // 2, x + n // 2, y)
        func(n // 2, x + n // 2, y + n // 2)

N, r, c = map(int, input().split())     # N, r, c 입력
answer = 0

func(2 ** N, 0, 0)
