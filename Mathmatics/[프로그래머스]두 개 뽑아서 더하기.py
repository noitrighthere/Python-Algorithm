from itertools import combinations

def solution(numbers):
    answer = []     # 결과 리스트
    temp = combinations(numbers, 2) # 조합으로 나타낼 수 있는 리스트를 만듬

    for i in temp:
        answer.append(i[0]+i[1])    # 조합의 값을 더함

    answer = list(set(answer))      # set함수를 사용하여 중복된 값을 제거
    answer.sort()                   # 오름차순

    return answer
