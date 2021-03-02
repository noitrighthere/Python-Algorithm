def solution(number, k):
    stack = []  # 스택 생성
    
    for i in number:

        while stack and i > stack[-1]:

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
