N, K = map(int, input().split())    # N: 국가의 수, K: 등수를 알고 싶은 국가
temp = [list(map(int, input().split())) for _ in range(N)]

# 금은동이 많은 개수대로 정렬
temp.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):
    # 국가에 해당하는 index를 설정
    if temp[i][0] == K:
        idx = i

for i in range(N):
    # 국가를 나타내는 index의 금은동 개수가 같으면 i+1을 해줌
    if temp[idx][1:] == temp[i][1:]:
        print(i+1)
        break
