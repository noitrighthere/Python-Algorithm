def solution(num):
    answer = 0      # 결과값

    while True:

        if num == 1:
            return answer
        answer += 1
        # 입력된 수가 짝수인 경우 2로 나눔
        if num % 2 == 0:
            num /= 2
        # 입력된 수가 홀수인 경우 3을 곱한후 1을 더함
        else:
            num = (num * 3) + 1

        if answer == 500:
            return -1
        
    return answer
