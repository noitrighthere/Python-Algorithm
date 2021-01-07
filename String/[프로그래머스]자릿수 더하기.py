def solution(n):
    # 숫자를 문자로 바꾸고 다시 숫자로 리스트에 넣어줌
    result = list(map(int, str(n)))
    return(sum(result))
