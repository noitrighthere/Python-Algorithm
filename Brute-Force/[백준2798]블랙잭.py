from itertools import combinations

N, M = map(int, input().split())        # 자연수 N, M 입력
card = list(map(int, input().split()))  # 카드 입력
result = 0

# combinations을 이용하여 모든 리스트의 조합을 구함
for i in combinations(card, 3):
    temp = sum(i)

    # M을 넘지 않으면서 최대한 M에 가까운 값을 찾음
    if result < temp <= M:
        result = temp

print(result)
