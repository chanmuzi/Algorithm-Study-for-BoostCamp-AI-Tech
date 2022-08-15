from collections import deque

end,start,target,up,down = map(int,input().split())
arr = [0] * (end + 1) # 최고 층수 + 1개 생성

def bfs():
    queue = deque([])
    queue.append(start)
    arr[start] = 1 # 방문 처리
    
    while queue:
        x = queue.popleft()
        
        if x == target: # 목표 도달하면
            return arr[x] - 1 # 함수 종료
        
        for nx in (x + up, x - down): # 위,아래 탐색
            # 범위를 만족하고 첫 방문인 경우
            if nx >= 1 and nx <= end and not arr[nx]:
                # 값을 업데이트하고 큐에 추가
                arr[nx] = arr[x] + 1
                queue.append(nx)
    # 목표에 도달하지 못하면 아무것도 return하지 않음                
    return

if start == target: # 시작층과 목표층이 같다면
    print(0)
else: # 그 외의 경우
    answer = bfs()
    # 목표층에 도착한 경우
    if answer: print(answer)
    # 목표층에 도착하지 못한 경우
    else: print("use the stairs")