def solution(a, b):
    answer = 0

    # 배열의 인덱스의 곱을 더함
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer
