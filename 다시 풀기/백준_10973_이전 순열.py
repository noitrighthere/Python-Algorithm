"""
백준 10973 이전 순열
난이도: 실버3
유형: 구현
"""

"""
from itertools import permutations

N = int(input())
arr = tuple(map(int, input().split()))

answer = []

# 순열로 만듦
permutation = list(permutations(arr, N))
# 오름차순으로 정렬
permutation.sort()

for i in range(len(permutation)):
    if arr == permutation[i]:
        if i == 0:
            print(-1)
        else:
            print(*permutation[i-1])
"""
N = int(input())
arr = list(map(int, input().split()))

k = -1
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        k = i

# 오름차순인 경우
if k == -1:
    print(-1)
else:
    for i in range(k+1, len(arr)):
        if arr[i] < arr[k]:
            m = i

    arr[k], arr[m] = arr[m], arr[k]

    temp = arr[k+1:]
    temp.sort(reverse=True)
    answer = arr[:k+1] + temp

    for num in answer:
        print(num, end = ' ')
    print()
