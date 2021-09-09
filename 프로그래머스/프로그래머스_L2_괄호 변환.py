"""
프로그래머스 괄호 변환
난이도: LV2
유형: 구현
"""
p = "()))((()"

def divide(w):
    temp = ''

    for i in range(len(w)):
        temp = w[:i+1]
        left = temp.count('(')
        right = temp.count(')')

        if left == right:
            u = temp
            v = w[i+1:]
            return(u, v)

def isBalanced(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    w = p

    # 과정 1
    if w == '':
        return ''
    
    # 과정 2
    u, v = divide(w)

    # 과정 3
    if isBalanced(u):
        # 과정 3-1
        u += solution(v)
        return u

    # 과정 4
    else:
        # 과정 4-1
        temp = '('
        # 과정 4-2
        v = solution(v)
        # 과정 4-3
        temp += v + ')'

        # 과정 4-4
        for s in u[1:-1]:
            if s == '(':
                temp += ')'
            else:
                temp += '('
                
    return temp

print(solution(p))

