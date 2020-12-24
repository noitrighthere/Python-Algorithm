N = int(input())
A = list(map(int, input().split()))     # 배열 A 입력
B = list(map(int, input().split()))     # 배열 B 입력

result = 0                              # 결과값

A.sort()                                # A는 오름차순
B.sort(reverse=True)                    # B는 내림차순

for i in range(N):
    result += A[i] * B[i]

print(result)
