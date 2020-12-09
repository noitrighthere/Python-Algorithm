n = int(input())    # 삼각형의 크기 n
triangle = []       # 삼각형을 담을 배열

for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
idx = 2             

for i in range(1, n):
    for j in range(idx):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif i == j:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
    idx += 1        # 층이 내려가면 인덱스 추가
    
print(max(triangle[n-1]))
        