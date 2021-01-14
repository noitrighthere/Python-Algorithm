def solution(s, n):

    answer = ''     # 결과값 
    temp = list(s)  # 문자를 리스트로 만듬

    for i in range(len(temp)):
        # 알파벳 26개, n을 더했을 때 z를 넘어갈 수도 있기 때문에 26으로 나눔
        # 대문자인 경우
        if temp[i].isupper():
            temp[i] = chr((ord(temp[i])-ord('A') + n) % 26 + ord('A'))
        # 소문자인 경우
        elif temp[i].islower():
            temp[i] = chr((ord(temp[i])-ord('a') + n) % 26 + ord('a'))

    answer = "".join(temp)
    return answer
