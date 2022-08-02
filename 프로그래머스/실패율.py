def solution(N, stages):
    users_list = [0] * (N+1)
    for i in stages:
        users_list[i-1] += 1
    print(users_list)
    fail = []
    stacked = 0
    for i in range(N):
        failure = users_list[i] / (len(stages) - stacked) if (len(stages) - stacked) else 0
        stacked += users_list[i]
        fail.append(failure)
    print(fail)
    fail_list = [(fail[x],x+1) for x in range(N)]
    fail_list.sort(key=lambda x:x[0], reverse=True)
    answer = [x[1] for x in fail_list]
    print(answer)
    return answer
    