s = str(input())

cnt = 0
# 숫자가 달라지면 count
for i in range(len(s)-1):
    if s[i] != s[i+1]: cnt += 1

# 0과 1일 때는 각각 0,1 출력    
if cnt == 0: print(0)
elif cnt == 1: print(1)
# 짝수일 때와 홀수일 때 나눠서 출력
elif cnt % 2 == 0:
    print(cnt//2)
else: print(cnt//2 + 1)
