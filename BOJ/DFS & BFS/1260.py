from collections import deque

n,m,v = map(int,input().split())

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)          

node = []
for i in range(m):
    x,y = map(int,input().split())
    node.append([x,y])

visited = [False] * (n+1)
case = [[0 for i in range(n+1)] for i in range(n+1)]
for i in node:
    x,y = i[0],i[1]
    case[x][y] = 1
    case[y][x] = 1
  
graph = []
for i in range(n+1):
    temp = []
    for j in range(n+1):
        if case[i][j] == 1:
            temp.append(j)
    graph.append(temp)

dfs(graph, v, visited)
print()

visited = [False] * (n+1)
bfs(graph, v, visited)    