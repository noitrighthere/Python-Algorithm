"""
프로그래머스 구명보트
난이도: LV2
유형: 그리디
"""
def solution(people, limit):
    answer = 0
    # 사람의 몸무게를 오름차순으로 정렬
    people.sort()

    i = 0
    j = len(people)-1
    
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
               
    return answer
