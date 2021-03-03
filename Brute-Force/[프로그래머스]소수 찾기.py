import math
from itertools import permutations

# n이 소수인지 판별하는 함수
def check_prime(n):
    # n이 1이하이면 소수가 아님
    if n <= 1:
        return False

    # 자기 자신 이외에 나누어 떨어지면 소수가 아님
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = []     # 정답을 답을 배열 생성

    for i in range(1, len(numbers)+1):
        # 모든 수의 조합을 구합
        temp = list(permutations(numbers, i))

        for j in range(len(temp)):
            # 임시변수에 있는 값들을 정수형으로 바꿔줌
            num = int(''.join(map(str, temp[j])))

            # 소수인지 판별해서 소수이면 정답 배열에 넣어줌
            if check_prime(num):
                answer.append(num)
    # 중복된 값을 제거
    answer = list(set(answer))
    return len(answer)
