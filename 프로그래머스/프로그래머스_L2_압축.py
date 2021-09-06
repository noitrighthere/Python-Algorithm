"""
프로그래머스 [3차]압축
난이도: LV2
유형: 구현, 문자열
"""
def solution(msg):
    answer = []
    dic = {}        # 딕셔너리 생성

    w, c = 0, 0
    
    for i in range(26):
        dic[chr(65+i)] = i+1

    while True:
        c += 1
        # 마지막 글자를 색인번호에 넣어줌
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break

        # w+c에 해당하는 단어가 없다면 사전에 추가
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c
    
    return answer
