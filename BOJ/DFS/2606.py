# 컴퓨터 수 n, 연결 쌍의 수 m
n = int(input())
m = int(input())

# 바이러스 걸린 컴퓨터 리스트
virus = []
# 탐색할 그래프, 시작점, 방문리스트
def dfs(graph, v, visited):
    global virus
    # 방문하면 True로 변환
    visited[v] = True
    # 바이러스 리스트에 추가
    virus.append(v)
    # 시작점의 연결점 중
    for i in graph[v]:
        # 방문하지 않은 곳이 있으면 방문
        if not visited[i]:
            dfs(graph, i, visited)

# 노드의 정보 입력 받기
node = []
for i in range(m):
    # 공백 기준 나눠서 노드 리스트에 추가
    x,y = map(int,input().split())
    node.append([x,y])

# 방문 여부 리스트
visited = [False] * (n+1)

# 연결 가능 여부 확인용 2차원 리스트 0으로 초기화
case = [[0 for i in range(n+1)] for i in range(n+1)]
# 노드의 정보로부터
for i in node:
    # 행 기준, 열 기준 둘 다 1로 변경
    x,y = i[0],i[1]
    case[x][y] = 1
    case[y][x] = 1

# 탐색에 사용할 최종 리스트    
graph = []
for i in range(n+1):
    # 임시 변수
    temp = []
    # 각 컴퓨터에 대해
    for j in range(n+1):
        # 연결된 컴퓨터 번호를 임시 변수에 추가
        if case[i][j] == 1:
            temp.append(j)
    # 연결 번호를 리스트로 최종 리스트에 추가
    graph.append(temp)

# 최종 리스트, 1번 시작, 방문 리스트
dfs(graph, 1, visited)

# 1번을 제외한 바이러스 컴퓨터 개수 출력
print(len(virus)-1)