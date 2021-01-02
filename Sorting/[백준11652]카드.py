N = int(input())    # 카드의 개수
dic = {}            # 딕셔너리 생성(key:value)

for _ in range(N):
    num = int(input())

    # 딕셔너리 value에 가지고 있는 카드 개수 추가
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

# 오름차순으로 정렬 후 가장 많은 수를 가지고 있고 가장 작은 수를 호출
dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])
