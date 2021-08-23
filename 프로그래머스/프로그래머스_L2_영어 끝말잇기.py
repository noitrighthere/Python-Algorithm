"""
프로그래머스 영어 끝말잇기
난이도: LV2
"""
def solution(n, words):
    answer = []

    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1,(i//n)+1]
    return [0, 0]
