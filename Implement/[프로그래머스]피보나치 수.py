def solution(n):
    num1, num2 = 0, 1

    while n > 0:
        num1, num2 = num2, num1+num2
        n -= 1
    answer = num1 % 1234567

    return answer
