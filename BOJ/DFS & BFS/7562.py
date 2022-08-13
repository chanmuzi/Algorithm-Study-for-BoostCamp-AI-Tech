from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1 # 시작 번호    
    while queue: # 더이상 움직일 곳이 없을 때까지
        x,y = queue.popleft()
        for i in range(8): # 8방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if [nx,ny] == target: # 타겟에 도착하면 결과 추가하고 종료
                results.append(graph[x][y])
                return
            # 범위를 벗어나면 다음 탐색
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 방문한 적이 있으면 패스
            if graph[nx][ny] != 0:
                continue
            # 방문한적이 없으면
            if graph[nx][ny] == 0:
                # 값을 갱신하고 큐에 추가
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                    
t = int(input())
for i in range(t):
    n = int(input())
    start = list(map(int,input().split()))  # 시작 위치
    target = list(map(int,input().split())) # 도착 위치

    if start == target: print(0) # 시작,도착 위치가 같은 경우
    else:    
        graph = [[0]*n for _ in range(n)] # 그래프 초기화
        
        # 방향 벡터
        dx = [2,1,-1,-2,-2,-1,1,2]
        dy = [1,2,2,1,-1,-2,-2,-1]
        results = []
        bfs(start[0],start[1]) # 탐색 후 최솟값 출력
        print(min(results))