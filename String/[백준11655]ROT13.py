S = list(map(str, input()))     # 문자열 입력
answer = ''     # 결과값

for i in range(len(S)):
    # 알파벳 26개, 13을 더했을 때 Z를 넘어갈 수도 있기 때문에 26으로 나눔
    if S[i].isupper():
        S[i] = chr((ord(S[i])-ord('A') + 13) % 26 + ord('A'))
    # 소문자인 경우
    elif S[i].islower():
        S[i] = chr((ord(S[i])-ord('a') + 13) % 26 + ord('a'))

answer = ''.join(S)
    
print(answer)
