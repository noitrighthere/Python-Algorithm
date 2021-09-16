"""
백준 2798 블랙잭
난이도: 브론즈2
유형: 완전탐색
"""
# N: 카드의 개수, M: 기준
N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            sum_value = arr[i] + arr[j] + arr[k]

            if sum_value <= M:
                answer = max(answer, sum_value)

print(answer)
