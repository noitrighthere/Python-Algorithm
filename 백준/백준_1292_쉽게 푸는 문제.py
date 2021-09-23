"""
백준 1292 쉽게 푸는 문제
난이도: 실버5
유형: 구현
"""
A, B = map(int, input().split())

arr = [0]

for i in range(B+1):
    for j in range(i):
        arr.append(i)

print(sum(arr[A:B+1]))
