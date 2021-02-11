N = int(input())    # 수열 A의 크기 N 입력
A = list(map(int, input().split())) # 수열 A

stack = []          #  스택
result = [-1 for _ in range(N)] # 답을 못찾을 경우 -1 출력을 위함

stack.append(0)
i = 1

# 스택에 값이 있고 수열의 크기가 i보다 클때
while stack and i < N:
    # 스택에 값이 있고 스택의 제일 위에 있는 인덱스 값이 수열 A의 인덱스 i보다 작을 때
    while stack and A[stack[-1]] < A[i]:
        result[stack[-1]] = A[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*result)
        
