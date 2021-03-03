def solution(number, k):
    stack = []  # 스택 생성
    
    for i in number:

        # 스택의 마지막 값이 넣으려고 하는 값보다 클 때
        while stack and i > stack[-1]:
            # 삭제할 수 있는 값이 아직 있으면 pop
            if k > 0:
                stack.pop()
                k -= 1

            else:
                break

        stack.append(i)

    if k > 0:
        for i in range(k):
            stack.pop()

    answer = "".join(stack)
    return answer

print(solution("1924", 2))
