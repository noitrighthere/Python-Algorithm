def func(arr):
    answer = 1
    cur = arr[0]        # 현재 기준점

    for i in range(1, len(arr)):
        # 현재 기준점 보다 다음 트로피가 더 높을 때
        if cur < arr[i]:
            answer += 1     # 보이는 트로피의 수를 1 추가하고 
            cur = arr[i]    # 현재 기준점을 다음 트로피로 교체

    return answer

N = int(input())        # 트로피 개수 입력
temp = []               # 트로피를 담을 배열

# 트로피 높이 입력
for _ in range(N):
    temp.append(int(input()))

print(func(temp))       # 왼쪽에서 봤을 때
temp.reverse()
print(func(temp))       # 오른쪽에서 봤을 때
