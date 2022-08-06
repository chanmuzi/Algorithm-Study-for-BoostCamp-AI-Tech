n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

answer = []
def dfs(x,y):
    global result
    if x < 0 or x >=n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        result += 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
    
                   
count = 0
for i in range(n):
    for j in range(n):
        result = 0
        if dfs(i,j) == True:
            count += 1
            answer.append(result)
print(count)
answer.sort()
for i in range(count):
    print(answer[i])