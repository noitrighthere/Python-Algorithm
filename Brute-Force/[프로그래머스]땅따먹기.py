def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 문자열 전체와 같은 열을 뺀 나머지 중 가장 큰 수를 구함
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]

    return max(land[len(land)-1])
