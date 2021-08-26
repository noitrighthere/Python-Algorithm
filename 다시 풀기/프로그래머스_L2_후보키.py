"""
프로그래머스 후보키
난이도: LV2
유형: 완전탐색
"""
from itertools import combinations

relation =[["100","ryan","music","2"],
           ["200","apeach","math","2"],
           ["300","tube","computer","3"],
           ["400","con","computer","4"],
           ["500","muzi","music","3"],
           ["600","apeach","music","2"]]

def solution(relation):
    answer = 0
    
    N = len(relation[0])
    key = list(range(N))

    candidates = []

    for i in range(1, N+1):
        for combi in combinations(key, i):
            temp = []
            for rel in relation:
                current_key = [rel[c] for c in combi]

                # 유일성을 확인
                if current_key in temp:
                    break
                else:
                    temp.append(current_key)
            else:
            # 최소성 확인
                for minimal in candidates:
                    if set(minimal).issubset(set(combi)):
                        break
                else:
                    candidates.append(combi)
    
    return len(candidates)

print(solution(relation))
