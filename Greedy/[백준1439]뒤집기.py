S = input()
cnt1 = 0    # 0으로 바뀌는 횟수
cnt2 = 0    # 1로 바뀌는 횟수

if S[0] == '0':
    cnt1 = 1
else:
    cnt2 = 1

for i in range(len(S)-1):
    # '0'과 '1'로 바뀌는 횟수를 계산
    if S[i] != S[i+1]:
        if S[i] == '0':
            cnt1 += 1
        else:
            cnt2 += 1
