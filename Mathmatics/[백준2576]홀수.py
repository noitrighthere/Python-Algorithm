temp = []           # 홀수를 담을 배열
result = 0          # 배열의 합

for i in range(7):

    n = int(input())

    # 자연수 n을 2로 나누었을 때 나머지가 0이 아니면 홀수
    if n % 2 != 0:
        temp.append(n)

for i in range(len(temp)):
        result += temp[i]

# 홀수가 없으면 -1 출력
if len(temp) == 0:
    result = -1
    print(result)

# 홀수들의 합과 홀수 중 최솟값 출력
else:
    print(result, min(temp))
