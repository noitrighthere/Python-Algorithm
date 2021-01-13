T = int(input())    # 테스트 케이스 개수

for _ in range(T):
    # A와 B를 콤마(,)로 구분
    A, B = map(int, input().split(','))
    result = A+B
    print (result)
