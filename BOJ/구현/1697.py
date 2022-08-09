from collections import deque

def bfs():
    # 큐 생성
    q = deque()
    q.append(n)
    
    # 큐가 빌 때까지
    while q:
        x = q.popleft()
        # k를 찾으면 종료
        if x == k:
            print(arr[x])
            break
        
        # x를 기준으로 다음 경우의 수 파악
        for nx in (x-1, x+1, x*2):
            # 범위 내 숫자이고 아직 처리하지 않은 숫자라면 +1
            if nx >= 0 and nx <= limit and not arr[nx]:
                arr[nx] = arr[x] + 1
                # 처리한 숫자를 기준으로 다시 반복
                q.append(nx)    

# 문제 조건을 기준으로 최댓값 설정
limit = 10**5 + 1
arr = [0] * (limit+1)
n,k = map(int,input().split())

bfs()