"""
프로그래머스 로또의 최고 순위와 최저 순위
난이도: LV1
유형: 구현
"""
# 몇 등인지 확인하는 함수
def check(value):
    if value == 6:
        return 1
    elif value == 5:
        return 2
    elif value == 4:
        return 3
    elif value == 3:
        return 4
    elif value == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    count = 0       # 맞은 로또를 체크
    wrong = 0       # 아닌 로또를 체크

    # 로또 번호를 체크하여 맞은 것과 0일 경우를 따짐
    for num in lottos:
        if num in win_nums:
            count += 1
        elif num == 0:
            count += 1
            wrong -= 1
        else:
            pass

    max_value = count
    min_value = count + wrong

    answer.append(check(max_value))
    answer.append(check(min_value))
    
    return answer
