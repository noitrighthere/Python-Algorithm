"""
백준 1759 암호 만들기
난이도: 골드5
유형: 완전탐색
"""
from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())
vowel = ['a', 'e', 'i', 'o', 'u']

arr.sort()

combi = combinations(arr, L)
result = []

for word in combi:
    
    count_vowel = 0     # 모음을 세는 변수
    count_cons = 0      # 자음을 세는 변수 

    for i in range(L):
        # 단어의 문자에 모음이 있으면 count_vowel += 1
        if word[i] in vowel:
            count_vowel += 1
        # 단어의 문자에 자음이 있으면 count_cons += 1
        else:
            count_cons += 1

    # 최소 모음이 하나 이상, 자음이 두개 이상
    if count_vowel >= 1 and count_cons >= 2:
        print(''.join(word))
