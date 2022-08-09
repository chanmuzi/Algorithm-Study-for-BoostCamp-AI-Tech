n,k = map(int,input().split())

def solution(n,k):
    # 카운트, 소수 리스트 초기화
    cnt = 0
    arr = [True] * (n+1)
    
    # 2부터 n까지에 대해
    for i in range(2,n+1):
        # 아직 건드린 적이 없는 수라면
        if arr[i]:
            # 자신을 포함한 배수를 False 처리
            for j in range(i,n+1,i):
                if arr[j] == True:
                    arr[j] = False
                    cnt += 1
                    # 처리마다 count해서 목표에 다다르면 반환
                    if cnt == k: return j
                    
print(solution(n,k))