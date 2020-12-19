N = int(input())    # 자연수 N 입력
result = 0

for i in range(1, N+1):
    # 1부터 99까지는 모두 한수
    if i < 100:
        result += 1
    # 자릿수대로 분리하여 등차수열이 맞는지 확인
    else:
        temp = list(map(int, str(i)))
        
        if temp[0] - temp[1] == temp[1] - temp[2]:
            result += 1

print(result)
