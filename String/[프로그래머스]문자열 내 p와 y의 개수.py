def solution(s):
    # 문자열을 소문자로 바꾸고 p와 y의 개수가 같은지 구함
    return (s.lower().count('p') == s.lower().count('y'))
