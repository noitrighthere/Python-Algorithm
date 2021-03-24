import sys

N = int(sys.stdin.readline())
temp = [0] * 10001

# 배열의 인덱스를 특정한 데이터의 값으로 설정
# 데이터가 등장한 횟수를 넣음
for i in range(N):
    num = int(sys.stdin.readline())
    temp[num] += 1

for i in range(10001):
    if temp[i] != 0:
        for j in range(temp[i]):
            print(i)
