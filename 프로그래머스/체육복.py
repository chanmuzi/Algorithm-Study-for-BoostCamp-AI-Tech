def solution(n, lost, reserve):
    cross = set(lost) & set(reserve)
    lost = list(set(lost)-cross)
    lost.sort()
    reserve = list(set(reserve)-cross)
    
    lost_copy = lost[:]
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            lost_copy.remove(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
            lost_copy.remove(i)
            
    return n-len(lost_copy)