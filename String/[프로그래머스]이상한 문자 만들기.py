def solution(s):
    
    temp = s.split(' ') # 공백 기준으로 문자열을 쪼갬
    result_arr = []     # 결과를 담을 배열

    for i in temp:
        result = ''
        
        for j in range(len(i)):
            # 글자 인덱스가 짝수 일 때
            if j % 2 == 0:
                result += i[j].upper()
            # 글자 인덱스가 홀수 일 때
            else:
                result += i[j].lower()
        result_arr.append(result)

    return(' '.join(result_arr))
