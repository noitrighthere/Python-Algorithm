N = int(input())    # 정수 N 입력
temp = list(map(int, input().split()))

# 중복된 값을 제거후 정렬
for i in sorted(list(set(temp))):
    print(i, end=' ')
