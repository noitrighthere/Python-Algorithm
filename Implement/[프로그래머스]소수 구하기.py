from itertools import combinations

"""
소수인지 판별하는 함수
"""
def isPrime(n1, n2, n3):
    num = n1 + n2 + n3  # 숫자의 합

    for i in range(2, num):
        # 1과 자신을 제외한 숫자로 나누었을 때 나눠지는 값이 있으면 소수가 아님
        if num % i == 0:
            return False

    return True

def solution(nums):
    answer = 0

    # 서로 다른 3개의 숫자의 조합을 구함
    temp = list(combinations(nums, 3))

    for i in temp:
        # 소수가 맞으면 +1을 함
        if isPrime(i[0], i[1], i[2]):
            answer += 1

    return answer

