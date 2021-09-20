"""
프로그래머스 [1차]프렌즈4블록
난이도: LV2
유형:
"""
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def solution(m, n, board):
    answer = 0
    # 2차원 배열로 만들어줌
    graph = list(map(list, zip(*board)))

    while True:
        # 사라질 블록을 담을 배열
        remove = [[0]*n for _ in range(m)]

        # 사라질 블록을 찾고 해당 위치를 remove에 1로 표시
        for i in range(m-1):
            for j in range(n-1):
                if graph[i][j] == graph[i+1][j] == graph[i][j+1] == graph[i+1][j+1]:
                    remove[i][j], remove[i+1][j], remove[i][j+1], remove[i+1][j+1] = 1, 1, 1, 1

        # 사라진 블록의 수를 세는 변수
        count = 0

        # remove에 담긴 1의 합을 구함
        for i in range(m):
            count += sum(remove[i])

        answer += count

        # 지워진 블록의 없는 경우 break
        if count == 0:
            break

        # 지워진 블록을 위의 블록이 떨어저 빈 공간을 채움
        for i in range(m-1, -1, -1):
            for j in range(n):
                if remove[i][j] == 1:
                    
                    x = i - 1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1

                        if x < 0:
                            graph[i][j] = 0
                        else:
                            graph[i][j] = graph[x][j]
                            remove[x][j] = 1
    return answer

print(solution(m, n, board))
