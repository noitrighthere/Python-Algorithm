def solution(name):
    # 알파벳에 대하여 최소 이동 값을 구함  
    temp = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    idx = 0
    answer = 0

    # 모든 리스트의 값이 0이 될때까지 반복
    while True:
        answer += temp[idx]
        temp[idx] = 0

        # 전부 다 계산이 되면 정답을 반환
        if sum(temp) == 0:
            break
        
        left, right = 1, 1      # 왼쪽, 오른쪽을 나타낼 변수 생성

        while temp[idx - left] == 0:
            left += 1

        while temp[idx + right] == 0:
            right += 1

        # 위치를 조정
        answer += left if left < right else right
        idx += -left if left < right else right
        
    return answer

print(solution("JEROEN"))
