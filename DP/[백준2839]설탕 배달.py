N = int(input())        # 배달해야 할 설탕 무게
result = 0              # 결과 값

while True:
    
    if N % 5 == 0:
        result = result + (N//5)
        print(result)
        break

    N = N - 3
    result += 1

    if N < 0:
        result = -1
        print(result)
        break
