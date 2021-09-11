"""
프로그래머스 모음 사전
난이도: LV2
유형: 문자열
"""
def solution(word):
    answer = 0

    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word)

    temp = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1

    for i in word:
        answer += temp * dic[i]
        temp = (temp - 1) // 5
    
    return answer
