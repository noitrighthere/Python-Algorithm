def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]  # 새로운 네트워크의 크기를 구함 

T = int(input())    # 테스트 케이스 입력

for _ in range(T):
    F = int(input())    # 친구 관계의 수 입력

    parent = dict()
    number = dict()

    for _ in range(F):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1   # 자신만 존재하기 때문에 네트워크의 크기는 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
