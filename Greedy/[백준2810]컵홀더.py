N = int(input())        # 좌석의 수
seat = input()
cnt = seat.count('LL')

if cnt <= 1:
    print(len(seat))
else:
    print(len(seat) - cnt + 1)
    



