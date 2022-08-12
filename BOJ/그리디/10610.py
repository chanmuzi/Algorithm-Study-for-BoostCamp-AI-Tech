n = list(str(input()))
# 내림차순 정렬
n.sort(reverse=True)

# 0이 없으면 불가능
if not '0' in n: print(-1)
else:
    # 3의 배수인지 확인
    three = 0
    for i in range(len(n)):
        three += int(n[i]) % 3
    three %= 3
    
    # 3의 배수가 아니면 불가능
    if three != 0:
        print(-1)
    # 2의 배수인지 확인
    else:            
        n = int(''.join(n))
        if n % 2 == 0:
            print(n)
        # 2의 배수가 아니면 불가능
        else: print(-1)