temp = [0]   # 기차에 있는 사람 수를 넣을 리스트

for i in range(4):
    a, b = map(int, input().split())    # a: 내린 사람, b: 탄 사람

    temp.append(temp[i] + b-a)          # 역 마다 사람의 수를 구함

print(max(temp))
