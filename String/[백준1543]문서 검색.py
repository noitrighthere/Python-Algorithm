document = input()  # 전체 문서 입력
word = input()      # 검색하고 싶은 단어

index = 0           # 문서검색 인덱스
answer = 0          # 결과값

# 검색하고 싶은 단어가 문서를 검색하는 시작점보다 길면 안됨
while len(document) - index >= len(word):
    # 문서에 검색하고 싶은 단어가 있을 때
    if document[index:index+len(word)] == word:
        answer += 1
        index += len(word)
    else:
        index += 1

print(answer)
