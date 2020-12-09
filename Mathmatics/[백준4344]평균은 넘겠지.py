C = int(input())    # 테스트 케이스 C 입력

for _ in range(C):
    temp = list(map(int, input().split(' ')))
    avg = sum(temp[1:]) / temp[0]   # 평균값 계산
    cnt = 0
    # 평균을 넘는 학생들의 비율을 반올림 
    for score in temp[1:]:
        if score > avg:
            cnt += 1
    print(str("%.3f" % round((cnt/temp[0])*100, 3)) + "%")
