T = int(input())    # 테스트케이스

for _ in range(T):
    x, y = map(int, input().split())    # x: 현재위치, y: 목표위치
    temp = y - x

    count = 0       # 이동 횟수
    move = 1        # 
    
