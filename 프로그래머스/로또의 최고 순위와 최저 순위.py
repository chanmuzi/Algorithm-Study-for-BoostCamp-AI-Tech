def solution(lottos, win_nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}

    cnt = 0
    zeros = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        elif i == 0:
            zeros += 1
    
    max_cnt = cnt + zeros
    min_cnt = cnt
    
    return [rank[max_cnt],rank[min_cnt]]