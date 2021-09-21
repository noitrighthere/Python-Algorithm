"""
백준 9613 GCD합
난이도: 실버3
유형: 수학
"""
import math

t = int(input())    # 테스트케이스

for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr.pop(0)  # 배열의 맨 앞이 n
    answer = 0

    for i in range(n):
        for j in range(n):
            # GCD는 a가 b보다 작아야 한다
            if i < j:
                # GCD의 합을 구함
                answer += math.gcd(arr[i], arr[j])

    print(answer)
