n = int(input())

# 키, 몸무게 리스트
people = list()
for i in range(n):
    people.append(list(map(int,input().split())))

# 등수 리스트
rank = list()
# 각 사람마다
for i in range(n):
    # 키와 몸무게 정보를 저장
    x,y = people[i]
    # 덩치가 더 큰 사람의 수
    temp = 0
    # 나머지 사람과 비교하며
    for j in range(n):
        # 키와 몸무게가 둘 다 더 큰 사람일 경우
        if x < people[j][0] and y < people[j][1]:
            # temp 증가
            temp += 1
    # 나머지 사람 조사후 등수 = 덩치 큰 사람수 + 1
    rank.append(temp+1)
    
print(*rank)