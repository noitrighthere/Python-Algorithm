"""
백준 1789 수들의 합
난이도: 실버5
유형: 그리디
"""
S = int(input())

N = 1
answer = 0

while True:
    S -= N

    if S >= 0:
        answer += 1
        N += 1

    else:
        print(answer)
        break
