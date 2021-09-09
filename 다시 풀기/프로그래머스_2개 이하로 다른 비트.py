"""
프로그래머스 2개 이하로 다른 비트
난이도: LV2
"""
numbers = [2,7]

def solution(numbers):
    answer = []

    for num in numbers:
        binary = list('0' + format(num, 'b'))

        index = ''.join(binary).rfind('0')
        binary[index] = '1'

        if num % 2 == 1:
            binary[index+1] = '0'

        answer.append(int(''.join(binary), 2))
    
    return answer

print(solution(numbers))
