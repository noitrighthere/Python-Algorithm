T = int(input())    # 테스트 케이스

for i in range(T):
    
    n = input()     # 'O', 'X' 입력
    result = 0      # 결과값
    cnt = 0         # 연속된 점수

    for j in range(len(n)):

        # 연속된 'O'값을 고려하여 계산
        if n[j] == 'O':
            cnt += 1
            result += cnt

        # 'X'이면 cnt을 0으로 초기화
        else:
            cnt = 0
            
    print(result)
