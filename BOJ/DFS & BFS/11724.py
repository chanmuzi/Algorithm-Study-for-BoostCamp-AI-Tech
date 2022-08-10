import sys
from collections import deque

def bfs(x):
    # 큐 생성
    queue = deque([x])
    # 방문 처리
    visited[x] = True
    # 큐가 빌 때까지
    while queue:
        temp = queue.popleft()
        # 연결된 노드 중 아직 방문하지 않은 것들을
        for i in graph[temp]:
            if not visited[i]:
                # 큐에 추가하고 방문 처리
                queue.append(i)
                visited[i] = True
  

n,m = map(int,input().split())
# 방문 처리할 리스트
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    # 무방향 그래프 생성
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
for i in range(1,n+1):
    # 방문 처리가 아직 안 되었을 때 count
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)