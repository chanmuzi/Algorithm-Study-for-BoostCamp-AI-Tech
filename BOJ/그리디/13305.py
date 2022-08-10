n = int(input())
# 각 도시별 거리, 비용
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))

# 현재 주유 가격
present = cost[0]
# 총 비용
pay = 0

# 도시 개수 -1 만큼 반복
for i in range(len(cost)-1):
    # 다음 도시에서 비용이 더 큰 경우
    if present < cost[i+1]:
        # 그대로 계산
        pay += distance[i] * present
    # 다음 도시의 비용이 더 작은 경우
    else:
        # 그 도시로 이동하고 주유 비용 변경
        pay += distance[i] * present
        present = cost[i+1]
print(pay)