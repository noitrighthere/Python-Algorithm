n = int(input())    # 자연수 n입력

tmp1 = 1
tmp2 = 2
result = 0

for i in range(1,n+1):
    if i == 1:
        result += 1
    elif i == 2:
        result += 1
    else:
        result = tmp1 + tmp2
        tmp1 = tmp2
        tmp2 = result

# 10007를 나눈 나머지 출력
print(result % 100007)
