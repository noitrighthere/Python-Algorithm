M = int(input())    # 자연수 M
N = int(input())    # 자연수 N

temp = []           # 소수를 담을 임시 배열

for i in range(M, N+1):
    if i == 1:
        pass
    elif i == 2:
        temp.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            elif j==i-1:
                temp.append(i)

if len(temp)==0:
    print(-1)
else:
    print(sum(temp))
    print(min(temp))
