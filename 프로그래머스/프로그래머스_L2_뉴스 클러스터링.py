"""
프로그래머스 뉴스 클러스터링
난이도: LV2
유형: 구현
"""
from collections import Counter

def solution(str1, str2):
    answer = 0

    # 두개의 원소를 무시해야 하니깐 대문자로 바꿈
    str1 = str1.upper()
    str2 = str2.upper()

    str1_list = []
    str2_list = []

    # 단어를 나눠서 배열에 넣음
    for i in range(len(str1)-1):
        # 특수문자나 공백이 아닌 이상 두글자씩 넣음
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i] + str1[i+1])

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i] + str2[i+1])

    # Counter함수를 이용
    counter_str1 = Counter(str1_list)
    counter_str2 = Counter(str2_list)

    # 교집합과 차집합으로 만듬
    intersection = list((counter_str1 & counter_str2).elements())
    union = list((counter_str1 | counter_str2).elements())

    if len(union) == 0 and len(intersection) == 0:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)
    
    return answer
