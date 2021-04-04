def solution(A,B):
    answer = 0      # 결과값

    # A를 오름차순 B를 내림차순으로 정렬(순서가 바뀌어도 상관없음)
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer
