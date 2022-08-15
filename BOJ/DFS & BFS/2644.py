import sys
from collections import deque

n = int(sys.stdin.readline())
visited = [0] * (n+1) # 방문 리스트
graph = [[] for _ in range(n+1)] # 연결 그래프
# 출발, 도착
start,end = map(int,sys.stdin.readline().split())

# 연결 그래프 생성
m = int(sys.stdin.readline())
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start,target,cnt):
    queue = deque([])
    queue.append(start)
    visited[start] = 0 # 0으로 시작
    
    while queue:
        temp = queue.popleft()
        # 연결된 노드 중에서
        for i in graph[temp]:
            # 아직 방문하지 않았다면
            if not visited[i]:
                # count하면서 방문 처리
                visited[i] = visited[temp] + 1
                queue.append(i)
                # 목표에 도착했으면 return
                if i == target:
                    return visited[i]
    # 목표에 도착하지 못했으면 -1
    return -1

# 시작,목표,count
answer = bfs(start,end,0)
print(answer)