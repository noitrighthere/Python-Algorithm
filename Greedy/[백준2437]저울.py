N = int(input())    # 저울추의 개수
temp = list(map(int, input().split()))
temp.sort()

count = 1           # 저울추가 나타낼 수 있는 양의 정수를 비교할 변수

for i in range(N):
    # 변수가 작으면 저울추가 나타낼 수 없는 최솟값
    if count < temp[i]:
        break
    count += temp[i]

print(count)
