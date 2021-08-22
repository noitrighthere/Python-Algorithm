"""
프로그래머스 실패율
난이도: LV1
유형: 구현
"""
def solution(N, stages):
    answer = {}         # 딕셔너리
    temp = len(stages)  # 스테이지에 도달한 플레이어의 수

    for stage in range(1, N+1):
        if temp != 0:
            count = stages.count(stage)
            answer[stage] = count/temp  # 각 스테이지당 실패율을 저장
            temp -= count               # 스테이지가 올라갈 수록 남아있는 사람의 수는 줄어듦
        # 다 깬 사람의 경우
        else:
            answer[stage] = 0
    
    return sorted(answer, key=lambda x:answer[x], reverse=True)
