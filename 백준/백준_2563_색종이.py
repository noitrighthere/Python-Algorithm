"""
백준 2563 색종이
난이도: 실버5
유형: 구현
"""
N = int(input())
# 도화지를 설정함
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())

    # 색종이를 도화지에 1로 넣음
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

answer = 0

# 영역의 넓이는 1의 개수
for i in paper:
    answer += i.count(1)

print(answer)
