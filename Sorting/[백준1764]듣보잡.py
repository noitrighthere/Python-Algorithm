N, M = map(int, input().split())    # N: 듣보 못한 사람, M: 보도 못한 사람

N_list = [input() for _ in range(N)]
M_list = [input() for _ in range(M)]

# 두 개의 리스트의 교집합을 구함
result = list(set(N_list) & set(M_list))

print(len(result))
# 결과 값을 사전 순으로 정렬 후 출력
for i in sorted(result):
    print(i)
