def solution(people, limit):
    answer = 0
    people.sort()   # 오름차순으로 만듬
    i = 0; j = len(people)-1

    while i <= j:
        answer += 1
        # 양 끝의 사람의 합이 기준에 맞으면 다음 사람을 구함
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    
    return answer
