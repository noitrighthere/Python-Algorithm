N = int(input())    # 자연수 N
temp = []           # 예상 등수
answer = 0

for _ in range(N):
    temp.append(int(input()))

# 오름차순으로 정렬
temp.sort()

for i in range(1, len(temp)+1):
    # 불만도 = (|A-B|)
    answer += abs(i-temp[i-1])

print(answer)
