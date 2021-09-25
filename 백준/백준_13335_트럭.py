"""
백준 13335 트럭
난이도: LV1
유형: 구현
"""
# n: 다리를 건너는 트럭의 수
# w: 다리의 길이
# L: 다리의 최대 하중
n, w, L = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
# 다리를 표현하는 스택 생성
stack = [0] * w

while len(stack) != 0:
    answer += 1
    stack.pop(0)

    if arr:
        # 다리를 건너는 트럭 + 대기하는 트럭의 무게가 견딜 수 있는 무게이면
        if sum(stack) + arr[0] <= L:
            # 대기하고 있던 트럭을 다리를 지나게 함
            stack.append(arr.pop(0))
        else:
            stack.append(0)

print(answer)
