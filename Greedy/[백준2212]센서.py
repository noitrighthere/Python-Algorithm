import sys

N = int(input())    # 센서의 개수
K = int(input())    # 집중국의 개수

# 집중국이 센서보다 많을 때
if K >= N:
    # 0을 출력하고 프로그램 종료
    print(0)
    sys.exit()

sensor = list(map(int, input().split(' '))) # 센서의 좌표

# 오름차순으로 정렬
sensor.sort()

temp = []   # 각 센서간의 거리를 구하기 위한 임시 배열

for i in range(1, N):
    temp.append(sensor[i]-sensor[i-1])
temp.sort(reverse=True)

# 가장 거리가 먼 순서대로 연결고리 제거
for i in range(K-1):
    temp[i] = 0

# 거리의 합을 구함
print(sum(temp))
