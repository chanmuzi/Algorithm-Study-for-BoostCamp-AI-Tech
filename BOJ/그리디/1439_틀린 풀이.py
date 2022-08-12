s = str(input())

cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]: cnt += 1
if cnt == 0 or cnt == 1: print(1)
elif cnt % 2 == 0:
    print(cnt//2)
else: print(cnt//2 + 1)
