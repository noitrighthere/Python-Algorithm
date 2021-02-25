N = int(input())        # 좌석의 수
seat = input()          # 좌석 입력
cnt = seat.count('LL')  # 커플 좌석의 수

# 커플 좌석이 1이하일때는 좌석의 수 만큼 가능
if cnt <= 1:
    print(len(seat))
else:
    print(len(seat) - cnt + 1)
    



