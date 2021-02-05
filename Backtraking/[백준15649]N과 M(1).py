from itertools import permutations

N, M = map(int, input().split())    # N, M 입력

temp = permutations(range(1, N+1), M)

for i in temp:
    print(' '.join(map(str, i)))
