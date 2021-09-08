"""
백준 2212 센서
난이도: 골드5
유형: 그리디
"""
import sys

N = int(input())    # 센서의 개수
K = int(input())    # 집중국의 개수

temp = []

if K >= N:
    print(0)
    sys.exit()

arr = list(map(int, input().split()))   # N개의 센서 좌표
arr.sort()  # 오름차순으로 정렬

# 각 센서 사이의 거리를 계산
for i in range(1, N):
    temp.append(arr[i] - arr[i-1])

# 가장 거리가 먼 순서대로 K-1 개의 연결 고리를 제거
temp.sort(reverse=True)

for i in range(K-1):
    temp[i] = 0

print(sum(temp))
