def solution(d, budget):
    d.sort()    # 부서 예산을 오름차순으로 정렬

    # 전체 부서별 신청 금액보다 예산이 크면 가장 큰 금액지원
    while budget < sum(d):
        d.pop() 
        
    return len(d)
