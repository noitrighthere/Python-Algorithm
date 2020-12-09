import sys
input = sys.stdin.readline

N = int(input())    # 정수 N입력
nList = list(map(int, input().split())) # 상근이가 갖고 있는 숫자 카드

M = int(input())    # 정수 M입력
mList = list(map(int, input().split())) # M개의 카드 리스트

nList.sort()    # 오름차순으로 정렬

# 이분탐색으로 해당 숫자를 찾음
for i in mList:
    low, high = 0, N
    while low <= high:
        mid = (low+high) // 2

        if 0 <= mid < N:
            if nList[mid] < i:
                low = mid + 1
            else:
                high = mid - 1
        else:
            break

    if 0 <= high + 1 < N:
        if nList[high+1] == i:
            print(1, end = ' ')
        else:
            print(0, end = ' ' )
    else:
        print(0, end = ' ')
    
