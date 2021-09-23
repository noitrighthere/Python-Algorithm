"""
프로그래머스 복서 정렬하기
난이도: LV1
유형: 정렬
"""
def solution(weights, head2head):
    answer = []
    rate = []
    
    for i in range(len(head2head)):
        win_count = 0           # 이긴 횟수
        weight_count = 0        # 자기보다 무거운 선수를 이긴 횟수
        no_count = 0            # 결과가 N일 때 세는 변수

        for j in range(len(head2head[i])):
            # 이겼을 때 승을 하나 추가
            if head2head[i][j] == "W":
                win_count += 1
                # 자기보다 무거운 선수를 이겼으면 이긴 횟수 추가
                if weights[i] < weights[j]:
                    weight_count += 1

            # 아직 붙어본 적이 없을 때
            elif head2head[i][j] == "N":
                no_count += 1

        if len(weights) - no_count != 0:
            # 승률, 자기보다 무거운 선수 이긴 횟수, 몸무게, 복서
            rate.append([(win_count / (len(weights) - no_count)) * 100, weight_count, weights[i], i])
        else:
            rate.append([0, weight_count, weights[i], i])

    # 승률 -> 자기보다 무거운 선수를 이긴 횟수 -> 몸무게 -> 복서 순으로 정렬(조건에 맞게)
    rate.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    for i in range(len(rate)):
        answer.append(rate[i][3] + 1)

    return answer
