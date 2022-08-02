import sys
n = int(input())

# 회의 시간 정보 리스트
con = []
for i in range(n):
    con.append(list(map(int,sys.stdin.readline().split())))
# 종료 시간, 시작 시간 기준 정렬
con.sort(key=lambda x:(x[1],x[0]))

# 회의 수 초기화
count = 0
start = -1
end = -1
for i in con:
    # 시작 시간이 끝 시간 이상이면
    if i[0] >= end:
        start = i[0]
        end = i[1]
        count += 1
    
print(count)