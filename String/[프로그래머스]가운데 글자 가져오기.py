def solution(s):
    temp = len(s)   # 단어의 길이를 나타내는 임시 변수

    # 단어의 길이가 홀수
    if temp % 2 != 0:
        return(s[temp//2])

    # 단어의 길이가 짝수
    else:
        # temp//2 - 1 <= LIST < temp//2 + 1
        return(s[temp//2 - 1:temp//2 + 1])
