"""
프로그래머스 메뉴 리뉴얼
난이도: LV2
유형: 조합
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            # 단품을 조합
            combo = combinations(sorted(order), c)
            temp += combo
        # 조합된 단품들이 몇개씩 들어갔는지 확인
        count = Counter(temp)

        # 코스 요리 만큼 주문한 손님이 있어야 하고 최소 2명 이상의 손님에게서 주문된 구성만 고름
        if len(count) != 0 and max(count.values()) != 1:
            for menu in count:
                # 가장 많이 함께 주문한 단품메뉴들만 코스요리로 만듦
                if count[menu] == max(count.values()):
                    answer.append(''.join(menu))
            
    return sorted(answer)
