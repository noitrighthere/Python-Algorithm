cnt = 0                 # 케이스를 나타낼 변수

while True:
    # L: 사용할 수 있는 일 수
    # P: 연속하는 일 수
    # V: 몇일짜리 휴가
    L, P, V = map(int, input().split())
    cnt += 1
    
    # L, P, V가 모두 0일 때 프로그램 종료
    if L + P + V == 0:
        break

    result = (V//P) * L     # 사용할 수 있는 휴가
    temp = V % P            # 사용할 수 있는 나머지 휴가

    # 나머지 조건을 확인
    if temp > L:
        result += L
    else:
        result += temp

    print("Case %d: %d" %(cnt, result))
    
