S = input()     # 문자열 S를 입력
temp = []       # 서로 다른 인덱스를 넣는 임시 배열

for i in range(len(S)-1):
    # 앞뒤가 다른 인덱스면 temp에 넣음
    if S[i] != S[i+1]:
        temp.append(S[i])

temp.append(S[-1])

print(min(temp.count('1'), temp.count('0')))
