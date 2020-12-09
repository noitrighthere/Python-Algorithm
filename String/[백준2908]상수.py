A, B = input().split()  # 변수 A, B를 입력

# A와 B를 거꾸로 뒤집어 준다.
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)
