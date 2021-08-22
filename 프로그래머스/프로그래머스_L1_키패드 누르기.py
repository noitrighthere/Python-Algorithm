"""
프로그래머스 키패드 누르기
난이도: LV1
유형: 구현
"""
def solution(numbers, hand):
    answer = ''
    last_left = 10      # '*'
    last_right = 12     # '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            last_left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            last_right = num
        else:
            # num이 0이면 11로 만들어줌
            num = 11 if num == 0 else num

            distance_left = abs(num - last_left)
            distance_right = abs(num - last_right)

            # 왼쪽의 차이가 오른쪽의 차이보다 클 경우: 오른쪽이 더 가까움
            if sum(divmod(distance_left, 3)) > sum(divmod(distance_right, 3)):
                answer += 'R'
                last_right = num
            # 반대의 경우: 왼쪽이 더 가까움
            elif sum(divmod(distance_left, 3)) < sum(divmod(distance_right, 3)):
                answer += 'L'
                last_left = num
            # 거리가 같을 경우
            else:
                if hand == "right":
                    answer += 'R'
                    last_right = num
                else:
                    answer += 'L'
                    last_left = num
    
    return answer
