"""
프로그래머스 완주하지 못한 선수
난이도: LV1
유형: 해시
"""
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for part, com in zip(participant, completion):
        if part != com:
            return part

    return participant[-1]

