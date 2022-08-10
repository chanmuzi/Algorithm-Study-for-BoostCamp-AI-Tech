s = int(input())

# 계산 결과, 카운트
result = 0
cnt = 0

# 계속 반복
while True:
    cnt += 1
    result += cnt
    
    # 계산 결과가 s보다 커지면 종료
    if result > s:
        break

print(cnt-1)