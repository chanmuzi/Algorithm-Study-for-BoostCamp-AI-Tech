import sys

n, m = map(int, sys.stdin.readline().split())
brand = []
for i in range(m):
    brand.append(list(map(int, sys.stdin.readline().split())))

miniset = min(i[0] for i in brand) # 세트 가격
minindi = min(i[1] for i in brand) # 낱개 가격

# 나머지가 0이 아니면서 세트 구매가 반드시 이득인 경우
if (n % 6) * minindi > miniset:  
    print(((n//6) + 1) * miniset)
# 6개 단위는 세트가 이득이지만 그 미만은 아닌 경우
elif 6 * minindi > miniset:
    print(miniset * (n//6) + minindi * (n % 6))
# 세트 가격 / 6 보다도 낱개가 저렴한 경우
else:
    print(n * minindi)