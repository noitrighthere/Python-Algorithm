X = int(input())    # X 입력
answer = 0

while X != 0:
    
    if X % 2 == 1:
        answer += 1

    X = X // 2
print(answer)
