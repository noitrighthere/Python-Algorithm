N = int(input())    # 자연수 N 입력
arr = set(map(int, input().split())) # N개의 정수 입력
M = int(input())
temp = list(map(int, input().split()))

for i in temp:
    if i not in arr:
        print('0')
    else:
        print('1')
