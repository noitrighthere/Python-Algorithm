"""
프로그래머스 방문 길이
난이도: LV2
유형: 구현
"""
def direction(d):
    # 위쪽으로 한 칸
    if d == "U":
        return 0
    # 아래쪽으로 한 칸
    elif d == "D":
        return 2
    # 오른쪽으로 한 칸
    elif d == "R":
        return 1
    # 왼쪽으로 한 칸
    elif d == "L":
        return 3
      
def solution(dirs):
    answer = 0

    # 위, 오른쪽, 아래, 왼쪽
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = set()
    x, y = 0, 0

    for d in dirs:
        i = direction(d)
        nx, ny = x + dx[i], y + dy[i]
        # 범위를 벗어날 경우 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        # 하나의 선분을 이동할 때 양방향을 같이 확인
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1
            
        x, y = nx, ny

    return answer
