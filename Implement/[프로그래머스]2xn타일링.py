def solution(n):
    answer = 0  # 결과값
    temp1 = 1   # n이 1일때 
    temp2 = 2   # n이 2일때

    # 재귀 호출을 사용하면 오래 걸리기 때문에 반복문을 사용
    while n > 1:
        temp1, temp2 = temp2, temp1+temp2
        n -= 1

    answer = temp1
    
    return answer % 1000000007
