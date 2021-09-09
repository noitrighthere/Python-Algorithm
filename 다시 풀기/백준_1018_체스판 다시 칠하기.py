"""
백준 1018 체스판 다시 칠하기
난이도: 실버5
유형: 브루트포스
"""
N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

result = []

# 체스판을 8x8로 고정시킴
for i in range(N-7):
    for j in range(M-7):

        first_w = 0
        first_b = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                # 행과 열의 합의 인덱스의 합이 짝수인 경우
                if (k+l) % 2 == 0:
                    if chess[k][l] != 'W':
                        first_w += 1
                    if chess[k][l] != 'B':
                        first_b += 1

                else:
                    if chess[k][l] != 'B':
                        first_w += 1
                    if chess[k][l] != 'W':
                        first_b += 1

        result.append(first_w)
        result.append(first_b)

print(min(result))
