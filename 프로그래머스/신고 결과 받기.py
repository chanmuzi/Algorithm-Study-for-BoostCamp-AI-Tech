n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))

def check(arr):
    maximum = 0
    colors = {'C':0,'P':1,'Z':2,'Y':3}

    for i in range(n):
        colors_count = [0,0,0,0]
        for j in range(n):
            colors_count[colors[arr[i][j]]] += 1
        if max(colors_count) > maximum:
            maximum = max(colors_count)
    
    for i in range(n):
        colors_count = [0,0,0,0]
        for j in range(n):
            colors_count[colors[arr[j][i]]] += 1
        if max(colors_count) > maximum:
            maximum = max(colors_count)
           
    return maximum

def convert(x,y):
    global arr
    maximum = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[x][y] == arr[nx][ny]: continue
        if arr[x][y] != arr[nx][ny]:
            arr[x][y],arr[nx][ny] = arr[nx][ny],arr[x][y]
            temp = check(arr)
            if temp > maximum:
                maximum = temp
            arr[x][y],arr[nx][ny] = arr[nx][ny],arr[x][y]
    return maximum

results = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(n):
        temp = convert(i,j) 
        results.append(temp)

print(max(results))
