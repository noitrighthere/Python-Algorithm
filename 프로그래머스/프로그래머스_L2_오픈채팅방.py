"""
프로그래머스 오픈채팅방
난이도: LV2
유형: 구현
"""
def solution(record):
    answer = []
    dic = {}
    
    for s in record:
        sentence = s.split()
        if len(sentence) == 3:
            dic[sentence[1]] = sentence[2]
            
    for s in record:
        sentence = s.split()
        if sentence[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[sentence[1]])
        elif sentence[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[sentence[1]])
            
    return(answer)
