N = int(input())    # 점의 개수 입력
temp = []

for _ in range(N):
    x, y = map(int, input().split())
    temp.append((x, y)) # 튜플 형태로 입력

temp = sorted(temp) # 오름차순으로 정렬

for i in temp:
    print(i[0], i[1])
