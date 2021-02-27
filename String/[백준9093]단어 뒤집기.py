import sys

input = sys.stdin.readline

T = int(input())    # 테스트 케이스 입력
temp = [list(input().split()) for i in range(T)]

for i in range(T):
    for j in temp[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()
