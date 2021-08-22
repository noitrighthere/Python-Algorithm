"""
프로그래머스 다리를 지나는 트럭
난이도: LV2
유형: 스택/큐
"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer
