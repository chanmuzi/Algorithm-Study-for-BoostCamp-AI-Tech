from collections import deque

c = int(input())

for i in range(c):
    n,m = map(int,input().split())
    imp_list = list(map(int,input().split()))
    imp_dict = [(x,imp_list[x]) for x in range(n)]
    queue = deque(imp_dict)
    
 
    answer = []

    while queue:
        flag = True
        if len(queue) == 1:
            temp = queue.pop()
            answer.append(temp)
        else:
            for i in range(1,len(queue)):
                if queue[0][1] < queue[i][1]:
                    temp = queue.popleft()
                    queue.append(temp)
                    flag = False
                    break
            if flag:
                temp = queue.popleft()
                answer.append(temp)
    
    for i in range(n):            
        if answer[i][0] == m:
            print(i+1)
            break