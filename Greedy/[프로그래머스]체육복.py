def solution(n, lost, reserve):

    reserve_temp = set(reserve) - set(lost)
    lost_temp = set(lost) - set(reserve)

    for i in reserve_temp:
        if i-1 in lost_temp:
            lost_temp.remove(i-1)
        elif i+1 in lost_temp:
            lost_temp.remove(i+1)
    
    return n-len(lost_temp)
