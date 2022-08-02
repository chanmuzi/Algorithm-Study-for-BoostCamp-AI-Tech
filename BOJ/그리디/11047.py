n,k = map(int,input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
    
count = 0
while k:
    for i in coin_list:
        if k // i == 0: continue
        else:
            count += k // i
            k %= i
print(count)