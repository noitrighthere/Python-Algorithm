"""
프로그래머스 단어 변환
난이도: LV3
유향: DFS/BFS
"""
def check(next_word, word):
    count = 0

    # zip 함수를 이용해서 단어의 알파벳이 맞는지 확인
    for a, b in zip(next_word, word):
        if a == b:
            count += 1

    # 한 단어만 바꿈 = 가장 짧은 변환 과정
    if count == len(word)-1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = [begin]     # 큐 생성

    # BFS 방식
    while queue:
        next_word = queue.pop()

        if next_word == target:
            return answer

        for i in range(len(words)):
            if not visited[i]:
                if check(next_word, words[i]):
                    visited[i] = True
                    queue.append(words[i])

        answer += 1
    
    return answer
