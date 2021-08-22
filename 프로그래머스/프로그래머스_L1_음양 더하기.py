"""
프로그래머스 음양 더하기
난이도: LV1
유형: 구현
"""
def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        # 불리언 배열의 인덱스가 True일 때
        if signs[i]:
            answer += absolutes[i]
        # 인덱스가 False 일 때
        else:
            answer -= absolutes[i]
    
    return answer
