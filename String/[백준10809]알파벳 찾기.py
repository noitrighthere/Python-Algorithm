S = input() # 단어 s
arr = [-1] * 26 # 알파벳 위치를 담을 배열 생성


for i in range(len(S)):
    if arr[ord(S[i])-97] != -1:
        continue
    else:
        arr[ord(S[i])-97] = i

for i in range(len(arr)):
    print(arr[i], end = ' ')
