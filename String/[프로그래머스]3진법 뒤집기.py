def solution(n):
    answer = 0
    temp = ''               # 3진법의 수를 담을 임시 변수 생성
    
    while n:
        temp += str(n % 3)  # 3으로 나눈 나머지의 값
        n = int(n / 3)      

    num = 1                 # 다시 10진수로 만들기 위한 변수
    for i in reversed(temp):
        answer += int(i) * num  # 3의 승수를 통해 다시 10진수로 변환 
        num *= 3
        
    return answer
