arr = []    # 알파벳을 담을 배열
word = input().upper()  # 대문자로 변환하여 단어 입력

# 단어에 있는 알파벳에 따라 배열로 나눔
for i in set(word):
    arr.append(word.count(i))

# idx에 최대값을 넣음
idx = [i for i, x in enumerate(arr) if x == max(arr)]

# idx의 길이가 2 이상이면 동일한 최대빈도가 2이므로 ?을 출력
if len(idx) >= 2:
    print("?")
else:
    print(list(set(word))[arr.index(max(arr))])