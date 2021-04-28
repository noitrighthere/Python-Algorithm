def solution(N, stages):

    rate = {}       # 딕셔너리 생성
    total = len(stages)
    
    for i in range(1, N+1):

        if total != 0:
            fail = stages.count(i)
            rate[i] = fail / total  # 실패율 계산
            total -= fail
        else:
            fail[i] = 0

    return sorted(rate, key=lambda x:rate[x], reverse=True)
