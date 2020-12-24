A, B, C = map(int, input().split()) # A : 시, B : 분, C : 초
D = int(input())                    # D : 요리하는 데 필요한 시간

# 초 단위 계산
C += D % 60
D = D // 60

if C >= 60:
    B += 1
    C -= 60

# 분 단위 계산
B += D % 60
D = D // 60

if B >= 60:
    A += 1
    B -= 60

# 시 단위 계산
A += D % 24

if A >= 24:
    A -= 24

print(A, B, C)
