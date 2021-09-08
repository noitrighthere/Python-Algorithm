"""
프로그래머스 조이스틱
난이도: LV2
유형: 그리디
"""

name = "JAZ"

def solution(name):
    answer = 0
    idx = 0
    temp = [min(ord(i) - ord('A'), ord('Z')-ord(i) + 1) for i in name]
    print(temp)

    while True:
        answer += temp[idx]
        temp[idx] = 0

        if sum(temp) == 0:
            break

        # 왼쪽, 오른쪽을 나타낼 변수
        left, right = 1, 1

        while temp[idx - left] == 0:
            left += 1

        while temp[idx + right] == 0:
            right += 1

        # 조이스틱 조작 횟수의 최솟값을 찾음
        answer += left if left < right else right
        # 커서 찾기
        idx += -left if left < right else right
    
    return answer

print(solution(name))
