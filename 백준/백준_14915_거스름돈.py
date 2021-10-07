"""
백준 14916 거스름돈
난이도: 실버5
유형: 그리디
"""
n = int(input())

value = n % 5

if n == 1 or n == 3:
    print(-1)

# 5로 나눈 값이 2로 떨어지면
elif value % 2 == 0:
    print(n//5 + value // 2)

# 2로 나누어 떨어지지 않으면    
else:
    print((n//5)-1 + (value+5)//2)

