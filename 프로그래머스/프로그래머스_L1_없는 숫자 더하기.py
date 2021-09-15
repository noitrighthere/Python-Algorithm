"""
프로그래머스 없는 숫자 더하기
난이도: LV1
유형: X
"""
def solution(numbers):
    answer = 0

    for num in range(10):
        if num not in numbers:
            answer += num
            
    return answer
