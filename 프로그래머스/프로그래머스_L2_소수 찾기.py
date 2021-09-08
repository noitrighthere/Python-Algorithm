"""
프로그래머스 소수 찾기
난이도: LV2
유형: 완전탐색
"""
from itertools import permutations

numbers = "011"

# 소수 구하기
def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True

def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers)+1):
        # numbers에 대한 모든 경우의 수를 만들어줌
        temp = list(map(''.join, permutations(numbers, i)))
        # 리스트에서 중복을 제거하고 소수를 구함
        for j in list(set(temp)):
            # 소수가 맞으면 answer에 넣음
            if isPrime(int(j)):
                answer.append(int(j))

    answer = len(set(answer))
    
    return answer

print(solution(numbers))
