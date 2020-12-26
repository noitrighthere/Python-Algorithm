N = int(input())    # 단어의 개수
temp = []           # 단어
alpha = [0 for _ in range(26)]
result = 0          # 결과값

for _ in range(N):
    temp.append(input())

for i in temp:
    idx = 0         # 각 자릿수를 나타내는 인덱스

    # 각 단어들이 위치한 자릿수를 알파벳마다 기록
    while i:
        cur = i[-1]
        alpha[ord(cur) - ord('A')] += pow(10, idx)
        idx += 1
        i = i[:-1]

alpha.sort(reverse = True) # 내림차순으로 정렬

# 큰 자릿수들에 위치한 알파벳부터 차례대로 계산
for i in range(9, 0, -1):
    result += i * alpha[9 - i]

print(result)
