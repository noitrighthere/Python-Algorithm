def solution(x, n):
    answer = []     # 결과 리스트
    
    for i in range(1, n+1):
        answer.append(x*i)

    return answer
