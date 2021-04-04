def solution(s):
    answer = True   # 결과값 플래그
    stack = []      # 괄호를 받을 스택

    for i in s:
        # '('가 들어오면 스택에 집어 넣음
        if i == '(':
            stack.append(i)

        # ')'가 들어오면 다음 조건을 확인
        elif i == ')':
            # 스택전체와 스택의 처음에 '(' 괄호가 있을 때 괄호를 없앰
            if stack and stack[-1] == '(':
                stack.pop()
            # 그게 아닐 시에는 False 처리
            else:
                answer = False
                break
    # 남아있는 스택의 유무와 플래그 확인
    if answer and not stack:
        return True
    else:
        return False
