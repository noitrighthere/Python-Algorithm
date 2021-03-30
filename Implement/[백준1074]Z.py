N, r, c = map(int, input().split())     # N, r, c 입력
answer = 0

while N > 0:
    temp = (2 ** N) // 2
    # 큰 사각형에서 점점 작은 사각형으로 이동
    if N > 1:
        # 2사분면
        if temp > r and temp <= c:
            answer += temp ** 2 # 1사분면 만큼 더해줌
            c -= temp
        # 3사분면
        elif temp <= r and temp > c:
            answer += (temp**2) * 2 # 2사분면 만큼 더해줌
            r -= temp
        # 1사분면
        elif temp <= r and temp <= c:
            answer += (temp**2) * 3 # 3사분면 만큼 더해줌
            r -= temp
            c -= temp

    # 2 x 2 일때 2~4 사분면을 이동한 횟수를 구함
    elif N == 1:
        if r == 0 and c == 1:
            answer += 1
        elif r == 1 and c == 0:
            answer += 2
        elif r == 1 and c == 1:
            answer += 3
    
    N -= 1

print(answer)
