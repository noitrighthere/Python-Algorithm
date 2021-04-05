def solution(s):
    answer = list(map(int, s.split()))  # 문자열 리스트를 정수로 바꿔줌

    # 최솟값과 최댓값을 구하면서 다시 문자열 형태로 변환
    return str(min(answer)) + " " + str(max(answer))
