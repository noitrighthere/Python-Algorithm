N = int(input())    # 새의 수 입력
answer = 0
K = 1

while N != 0:

    if K > N:
        K = 1
    else:
        N -= K
        K += 1
        answer += 1

print(answer)
