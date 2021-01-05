def solution(n):

    answer = ''
    
    for i in range(n):
        # n이 짝수이면
        if i % 2 == 0:
            answer += "수"
        # n이 홀수이면
        else:
            answer += "박"

    print(answer)

solution(8)
