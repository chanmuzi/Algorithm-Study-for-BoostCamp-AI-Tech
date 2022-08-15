import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 설정

squares = [] # 사각형 정보를 담을 리스트
m,n,k = map(int,sys.stdin.readline().split())
for i in range(k):
    squares.append(list(map(int,sys.stdin.readline().split())))

graph = [[0 for _ in range(n)] for _ in range(m)] # 좌표 초기화

for a,b,c,d in squares: # 사각형의 정보를 토대로
    start_row = m - d   # 행렬에 적용할 좌표로 변환
    end_row = m - b
    start_col = a
    end_col = c
    
    # 사각형 면적에 포함되는 좌표값 1로 변경
    for row in range(start_row,end_row):
        for col in range(start_col,end_col):
            graph[row][col] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global cnt # 전역 변수 선언
    
    # 범위 벗어나면 무시
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    # 이미 1인 좌표 무시
    if graph[x][y] == 1:
        return False
    
    # 방문한 적 없으면 방문 처리 후 카운트
    if graph[x][y] == 0:
        graph[x][y] = 1
        cnt += 1
        
        for i in range(4): # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True # 탐색 후 True 반환
    
    return False        

results = [] # 영역 넓이를 담을 리스트
area = 0
for i in range(m): # 직사각형 전체 탐색
    for j in range(n):
        cnt = 0
        if dfs(i,j): # 탐색이 가능했다면
            area += 1 # 영역 개수 추가
            results.append(cnt) # 누적된 카운트 추가

results.sort() # 오름차순 정렬
print(area)
print(*results)