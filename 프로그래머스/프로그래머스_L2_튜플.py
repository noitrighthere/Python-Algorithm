"""
프로그래머스 튜플
난이도: LV2
유형: 정렬, 문자열
"""
def solution(s):
    answer = []

    # 문자열을 자른 후
    # 길이대로 정렬
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = lambda x : len(x))

    for i in s:
        temp = i.split(',')
        for j in temp:
            # 튜플안에 원소가 없으면 없는 원소를 튜플에 넣어줌
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer
