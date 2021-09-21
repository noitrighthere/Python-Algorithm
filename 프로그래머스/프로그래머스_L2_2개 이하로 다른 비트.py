"""
프로그래머스 2개 이하로 다른 비트
난이도: LV2
유형: 그리디
"""
def solution(numbers):
    answer = []

    for num in numbers:
        # 2진수로 만들어줌
        binary = list('0' + format(num, 'b'))

        # 오른쪽에서부터 0이 어디에 위치해 있는지 찾음
        temp = ''.join(binary).rfind('0')
        binary[temp] = '1'

        # num이 홀수이면
        if num % 2 == 1:
            binary[temp+1] = '0'

        # 2진수를 다시 10진수로 변환
        answer.append(int(''.join(binary), 2))
        
    return answer
