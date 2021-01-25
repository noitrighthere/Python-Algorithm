M = int(input())    # 자연수 M
N = int(input())    # 자연수 N

temp = []           # 소수를 담을 임시 배열
answer_sum = 0      # 소수의 합

def is_prime_number(x):

    # 2부터 (x-1)까지의 모든 수를 확인
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어지면 소수가 아님
        if x % i == 0:
            return
    # 배열에 해당 수를 넣음
    temp.append(x)  

# M이상 N이하 자연수 중 소수를 찾음
for i in range(M, N+1):
    is_prime_number(i)

# 소수의 합을 구함
for i in temp:
    answer_sum += i

if len(temp) > 0:
    print(answer_sum, min(temp))
else:
    print(-1)




