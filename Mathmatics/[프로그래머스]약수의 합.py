def solution(n):
    answer = 0      # 결과값   

    for i in range(1, n+1):

        # 1부터 n까지의 숫자중 나누어서 나머지가 없으면 약수
        if (n % i) == 0:
            answer += i
    
    return answer
