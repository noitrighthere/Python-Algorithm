def solution(x):
    answer = True
    temp = list(map(int, str(x)))   # 양수 x를 문자열 리스트로 만듬
    temp_sum = 0        # x의 자릿수 합

    for i in temp:
        temp_sum += int(i)

    # 하샤드 수
    if x % temp_sum == 0:
        return answer
    else:
        return False
