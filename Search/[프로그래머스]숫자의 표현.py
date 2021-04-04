def solution(n):
    answer = 0

    for i in range(1, n+1):
        temp = 0        # 자연수를 더한 값이 n하고 일치하는지 확인하기 위한 임시 변수

        for j in range(i, n+1):
            temp += j   # 연속된 자연수를 더함
            # 임시 변수가 n에 일치하는 경우: 해당
            if temp == n:
                answer += 1
                break
            # 임시 변수가 n보다 큰 경우: 해당 안됨
            if temp > n:
                break
    
    return answer
