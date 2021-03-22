T = int(input())    # 테스트케이스 입력

for _ in range(T):
    left_stack = []
    right_stack = []
    k = input()     # 키보드 명령어 입력

    for i in k:
        # '-' 입력 시 왼쪽 스택에서 원소 제거
        if i == '-':
            if left_stack:
                left_stack.pop()
        # '<' 입력 시 왼쪽 스택에서 오른쪽 스택으로 이동
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        # '>' 입력 시 오른쪽 스택에서 왼쪽 스택으로 이동
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    # 왼쪽 스택과 오른쪽 스택을 합침
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
