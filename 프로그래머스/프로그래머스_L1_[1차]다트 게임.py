"""
프로그래머스 [1차]다트 게임
난이도: LV1
유형: 스택 / 큐
"""
def solution(dartResult):
    answer = 0
    score = []
    num = ''
    
    for dart in dartResult:
        if dart.isnumeric():
            num += dart
        elif dart == 'S':
            num = int(num) ** 1
            score.append(num)
            num = ''
        elif dart == 'D':
            num = int(num) ** 2
            score.append(num)
            num = ''
        elif dart == 'T':
            num = int(num) ** 3
            score.append(num)
            num = ''
        elif dart == '*':
            if len(score) > 1:
                # 해당 점수와 해당 전 전수를 2배로 만든다.
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif dart == '#':
            score[-1] = score[-1] * -1

    answer = sum(score)
    
    return answer
