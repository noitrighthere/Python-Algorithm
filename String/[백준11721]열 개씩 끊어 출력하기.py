S = input() # 단어 S

# 10의 배수로 끊어 문자를 출력
for i in range(0, len(S), 10):
    print(S[i:i+10])

