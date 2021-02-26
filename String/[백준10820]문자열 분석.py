import sys

while True:

    word = sys.stdin.readline().rstrip('\n')

    # 문장이 없으면 끝남
    if not word:
        break

    cnt1 = 0    # 소문자
    cnt2 = 0    # 대문자 
    cnt3 = 0    # 숫자
    cnt4 = 0    # 공백

    for i in word:
        # 소문자 일 때
        if i.islower():
            cnt1 += 1
        # 대문자 일 때
        elif i.isupper():
            cnt2 += 1
        # 숫자 일 때
        elif i.isdigit():
            cnt3 += 1
        # 공백 일 때
        elif i.isspace():
            cnt4 += 1

    print(cnt1, cnt2, cnt3, cnt4)
