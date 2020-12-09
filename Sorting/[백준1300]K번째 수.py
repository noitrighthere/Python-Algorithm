N, K = map(int, input().split())    # N: N의 수, K: K번째 수

temp = list(map(int, input().split()))
temp.sort()

print(temp[K-1])    # K번째 수를 호출
