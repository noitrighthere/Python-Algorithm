from math import gcd

def solution(n, m):
    answer = []     # 결과값
    temp = 0        # 최소공배수를 담을 변수
    
    def lcm(n, m):
        temp = n * m // gcd(n, m)
        return temp

    # 최대공약수와 최소공배수를 리스트에 더함
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))

    return answer
