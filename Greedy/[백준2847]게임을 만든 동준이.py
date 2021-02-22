N = int(input())    # 레벨의 수
temp = [int(input()) for _ in range(N)]    # 점수 입력
answer = 0          # 감소한 횟수

# 맨 마지막 레벨부터 시작
for i in range(N-1, 0, -1):
    # 낮은 레벨이 높은 레벨보다 점수가 클 경우
    if temp[i] <= temp[i-1]:
        # 횟수를 구하고 낮은 레벨은 높은 레벨보다 -1 인 점수를 줌
        answer += (temp[i-1]-temp[i]) + 1
        temp[i-1] = temp[i]-1

print(answer)
