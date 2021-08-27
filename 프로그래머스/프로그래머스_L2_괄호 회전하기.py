"""
프로그래머스 괄호 환전하기
난이도: LV2
유형: 큐
"""
from collections import deque

def check(queue):
    stack = []

    for c in queue:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            s = stack.pop()

            if s != '(' and c == ')':
                return False
            elif s != '[' and c == ']':
                return False
            elif s != '{' and c == '}':
                return False

    return len(stack) == 0

def solution(s):
    answer = 0
    queue = deque(s)

    # 괄호를 회전시키면서 하나씩 검사
    for _ in range(len(s)):
        q = queue.popleft()
        queue.append(q)

        # 올바른 괄호라면 +1
        if check(queue):
            answer += 1
    
    return answer
