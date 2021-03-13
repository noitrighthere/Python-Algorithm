import sys

N = int(input())    # 크레인 수 입력
crane = list(map(int, input().split())) # 크레인 무게 제한 입력

M = int(input())    # 박스 수 입력
box = list(map(int, input().split()))   # 박수 무게 입력

cnt = 0             # 박스를 옮긴 횟수 
answer = 0

# 박스를 옮길 수 없는 경우
if max(crane) < max(box):
    print(-1)
    sys.exit()

position = [0] * N  # 각 크레인이 현재 옮겨야 하는 박스의 번호
check = [False] * M # 각 박스를 옮겼는지 여부

# 크레인과 박스를 내림차순 정렬
crane.sort(reverse=True)
box.sort(reverse=True)

while True:
    if cnt == len(box):
        break

    # 모든 크레인에 대하여 처리
    for i in range(N):
        while position[i] < len(box):
            # 아직 옮겨지지지 않은 박스 중에서 옮길 수 있는 박스를 만날 때까지 반복
            if not check[position[i]] and crane[i] >= box[position[i]]:
                check[position[i]] = True
                position[i] += 1
                cnt += 1
                break
            position[i] += 1
    answer += 1

print(answer)
