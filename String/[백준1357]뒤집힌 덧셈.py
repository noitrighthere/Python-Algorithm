def Rev(num):
    temp = int(str(num)[::-1])      # 정수를 뒤집음
    
    return temp

X, Y = map(int, input().split())    # 정수 X, Y 입력

print(Rev(Rev(X)+Rev(Y)))
