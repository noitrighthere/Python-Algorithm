def solution(s):
    # 문자열의 길이가 4 혹은 6일 때
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            # 문자당 숫자인지 아닌지 판별(문자가 하나라도 나오면 바로 결과 출력)
            if not s[i].isdigit():
                return False
        return True
    else:
        return False
