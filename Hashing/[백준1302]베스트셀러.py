N = int(input())    # 팔린 책의 개수
books = {}           # 책 딕셔너리 새성

for _ in range(N):
    i = input()
    # 새로운 책이라면 1 생성
    if i not in books:
        books[i] = 1
    # 동일한 책이면 1 추가
    else:
        books[i] += 1

temp = max(books.values())
arr = []

# key와 value를 한번에 for문으로 사용하기 위해 items() 사용
for key, value in books.items():
    # 가장 많이 팔린 책인 여러개인 경우 고려해서 배열에 넣음
    if value == temp:
        arr.append(key)

print(sorted(arr)[0])
