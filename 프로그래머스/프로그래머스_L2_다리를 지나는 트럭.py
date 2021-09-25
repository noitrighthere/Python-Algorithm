"""
프로그래머스 다리를 지나는 트럭
난이도: LV2
유형: 스택/큐
"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리를 표현하는 스택 생성
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            # 다리를 건너고 있는 트럭과 대기하고 있는 트럭의 무게가 견딜 수 있는 무게라면
            if sum(bridge) + truck_weights[0] <= weight:
                # 대기하고 있는 트럭을 다리를 건너게 함
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer
