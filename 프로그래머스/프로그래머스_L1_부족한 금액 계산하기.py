"""
프로그래머스 부족한 금액 계산하기
난이도: LV1
유형:
"""
def solution(price, money, count):
    answer = -1
    total = 0

    for i in range(1, count+1):
        total += (price*i)

    answer = total - money

    if answer <= 0:
        return 0

    return answer
