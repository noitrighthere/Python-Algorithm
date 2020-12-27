def solution(arr, divisor):

    answer = []     # 결과값

    for i in arr:

        # element가 divisor로 나누어 떨어지면 배열에 추가
        if i % divisor == 0:
            answer.append(i)

    answer.sort()   # 오름차순으로 정렬
    
    if len(answer) == 0:
        answer.append(-1)
        return(answer)

    else:
        return(answer)
