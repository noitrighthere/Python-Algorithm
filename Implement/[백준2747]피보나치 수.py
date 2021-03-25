N = int(input())

# 피보나치 수는 0과 1로 시작
num1 = 0
num2 = 1

# 반복문을 사용하여 피보나치 수를 구함
while N > 0:
    num1, num2 = num2, num1 + num2
    N -= 1

print(num1)
