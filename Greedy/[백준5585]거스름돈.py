money = [500, 100, 50, 10, 5, 1]    # 화폐 단위
N = 1000 - int(input())    # 지불한 돈 입력하여 거스름 돈 생성
cnt = 0

for i in money:
    cnt += N // i   # 한번 거슬러 줄 수 있음
    N %= i

print(cnt)
